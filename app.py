from flask import Flask, request, redirect
import os
import requests
from coordinates import Location
from breweries import Brewery
from map import Map
import json
from haversine import haversine, Unit


from flask.templating import render_template
app = Flask(__name__)

# Routes 
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def root():
    def get_beer():
        # gets JSON for random beer from Robert Baucus's microservice
        response = requests.get('http://127.0.0.1:42001')
        return response.json()

    def process_name(name: str) -> str:
        # returns string with title case and underscores replaced with blank spaces
        return name.replace('_', ' ').title()
    
    # Gets beer name, image, and description from microservice for display on page
    beer = get_beer()
    beer_title = process_name(beer['beer_image'][0])
    beer_image = beer['beer_image'][1]
    beer_descript = beer['beer_description'][1]
    
    return render_template("home.html", beerTitle=beer_title, beer=beer_image, beerDescript=beer_descript)

@app.route('/results', methods=['POST'])
def get_results():
    
    zip_code = request.form['zip']
    gps = request.form['gps']
    range = request.form['range']
    filter = request.form['breweryType']

    # processing functions
    def process_type(type: str) -> str:
        # Converts to title case and improves clarity of a brewery category name
        return "Microbrewery" if type == 'micro' else type.title()

    def process_gps(coords: str) -> list:
        # split string into 2, separated by comma
        lat = ''
        lon = ''
        cur = 1
        for char in coords:
            if char == ",":
                cur = 2
            else:
                if cur == 1:
                    lat += char
                else:
                    lon += char
        return [lat, lon]

    # create and validate user location that has latitude/longitude
    if gps == "":
        user_location = Location(zip_code)
    else:
        coords = process_gps(gps)
        user_location = Location(zip_code, coords[0], coords[1])
    if not user_location.get_is_valid():
        return redirect('/home')

    area = Map(user_location, range) # creates Map object which will hold user's location, and list of selected breweries.
    range = area.get_range()  # creation of range also validates it in get_range() method

    # get the 20 closest breweries to coordinates
    data = requests.get('https://api.openbrewerydb.org/breweries?by_dist='+user_location.get_y()+','+user_location.get_x()+'&per_page=20')
    breweries = json.loads(data.text)  # convert object to json

    """ LOOP:
    Creates Location object for each brewery, and a Brewery object which holds that location and other brewery info such as 
    brewery type and URL. Each brewery's distance from user is calculated using a method called from the user's Location object.
    If each brewery's distance is within the user's established range, and meets any filter requirements, the brewey is selected.
    Finally, that brewery is appended to the Map object.
    """
    for brewery in breweries:
        brewery_location = Location(brewery['postal_code'], brewery['latitude'], brewery['longitude'])
        new_brewery = Brewery(brewery['name'], process_type(brewery['brewery_type']), brewery_location, brewery['website_url'])
        distance = user_location.calc_distance(new_brewery.get_location())
        new_brewery.set_distance(round(distance, 2))

        if distance <= range:
            if filter == 'ALL' or new_brewery.get_type() == filter:
                new_brewery.select()

        area.add_brewery(new_brewery)

    # Load selected breweries into a list for display to the user, and get any wiki summaries available for those breweries.
    area.select_breweries() 
    area.set_wiki_summaries()

    if gps == "":
        searched_loc = user_location.get_zip()
    else:
        searched_loc = "your location"

    return render_template('results.html', results=area.get_selected_breweries(), user_loc=searched_loc, 
     range=area.get_range(), filter=filter)

if __name__ == '__main__':
   app.run()