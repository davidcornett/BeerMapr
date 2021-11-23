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

    # create and validate user location that has latitude/longitude
    user_location = Location(zip_code) # creates Location object for user
    if not user_location.get_is_valid():
        return redirect('/home')

    area = Map(user_location, range) # creates Map object which will hold user's location, and list of selected breweries.
    range = area.get_range()  # creation of range also validates it in get_range() method

    # PRODUCTION version
    # get the 20 closest breweries to coordinates
    data = requests.get('https://api.openbrewerydb.org/breweries?by_dist='+user_location.get_y()+','+user_location.get_x()+'&per_page=20')
    breweries = json.loads(data.text)  # convert object to json
    """ ---------------------------------------------------
    # TEST version, does not use API 
    f = open('breweries.json')
    breweries = json.load(f)
    f.close()
    ------------------------------------------------------
    """
    def process_type(type: str) -> str:
        # Converts to title case and improves clarity of a brewery category name
        return "Microbrewery" if type == 'micro' else type.title()

    """ LOOP:
    Creates Location object for each brewery, and a Brewery object which holds that location and other brewery info such as 
    brewery type and URL. Each brewery's distance from user is calculated using a method called from the user's Location object.
    If each brewery's distance is within the user's established range, and meets any filter requirements, the brewey is selected.
    Finally, that brewery is appended to the Map object.
    """
    for brewery in breweries:
        brewery_location = Location(brewery['postal_code'], brewery['longitude'], brewery['latitude'])
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
    return render_template('results.html', results=area.get_selected_breweries(), zip_code=user_location.get_zip(), range=area.get_range(), filter=filter)


@app.route('/test')
def test():
    def get_wiki_summary(attraction: str):
        """
        Returns JSON containing wikipedia summary test for your desired attraction
        Takes any string - process_string() ensures title case and blank spaces will be processed
        """

        def process_string(string: str) -> str:
            new_string = string.title()  # capitalize all words (some wiki entries are case sensitive)
            return new_string.replace(' ', '_')  # return string with blank spaces replaced with underscores
        attraction = process_string(attraction)  # process attraction's name to work with wikipedia search

        # gets JSON containing wikipedia summary for URL parameter
        response = requests.get('http://127.0.0.1:9999/'+attraction)
        wiki_summary = response.json()  # conver to JSON
        return wiki_summary

    #response = requests.get('https://api.github.com')
    #response = requests.get('https://api.openbrewerydb.org/breweries?by_dist=38.87418813900499,-77.30317040648194&per_page=50')
    #response = requests.get('https://api.openbrewerydb.org/breweries/12432')
    #print(response.text)
    return get_wiki_summary()

if __name__ == '__main__':
   app.run()