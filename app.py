from flask import Flask, request
import os
import requests
from coordinates import Location
from breweries import Brewery
from map import Map
import json
from haversine import haversine, Unit

import pgeocode

from flask.templating import render_template
app = Flask(__name__)

# Routes 
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def root():
    def get_beer():
        # gets JSON for random beer from Robert Baucus's microservice
        response = requests.get('http://127.0.0.1:42001')
        beer = response.json()
        return beer
    beer = get_beer()
    print(beer)
    
    return render_template("home.html")

@app.route('/results', methods=['POST'])
def get_results():

    zip_code = request.form['zip']
    range = request.form['range']
    filter = request.form['breweryType']

    # convert range from str to int, with default of 30 used if blank
    try:
        range = int(range)
    except:
        range = 30

    # create user location that has latitude/longitude
    user_location = Location(zip_code)
    area = Map(user_location)

    """production version
    # get the 20 closest breweries to coordinates
    data = requests.get('https://api.openbrewerydb.org/breweries?by_dist='+user_location.get_y()+','+user_location.get_x()+'&per_page=20')
    breweries = json.loads(data.text)  # convert object to json
    """
    # test version----------------------------------------
    f = open('breweries.json')
    breweries = json.load(f)
    f.close()
    #------------------------------------------------------

    def process_type(type: str) -> str:
        return "Microbrewery" if type == 'micro' else type.title()

    for brewery in breweries:
        brewery_location = Location(brewery['postal_code'], brewery['longitude'], brewery['latitude'])
        new_brewery = Brewery(brewery['name'], process_type(brewery['brewery_type']), brewery_location, brewery['website_url'])
        distance = user_location.calc_distance(new_brewery.get_location())
        new_brewery.set_distance(round(distance, 2))

        if distance <= range:
            if filter == 'ALL' or new_brewery.get_type() == filter:
                new_brewery.select()

        area.add_brewery(new_brewery)
        #print(new_brewery.get_distance()-int(range))

    area.select_breweries()  # creates list of selected breweries to display to the user
    area.set_wiki_summaries()
    return render_template('results.html', results=area.get_selected_breweries(), zip_code=user_location.get_zip(), range=range, filter=filter)

@app.route('/test')
def test():
    def get_wiki_summary():
        attraction = 'Empire_State_Building'
        # gets JSON containing wikipedia summary for URL parameter
        response = requests.get('http://127.0.0.1:9999/'+attraction)
        #response = requests.get('http://127.0.0.1:9999/Empire_State_Building')
        wiki_summary = response.json()
        return wiki_summary

    #response = requests.get('https://api.github.com')
    #response = requests.get('https://api.openbrewerydb.org/breweries?by_dist=38.87418813900499,-77.30317040648194&per_page=50')
    #response = requests.get('https://api.openbrewerydb.org/breweries/12432')
    #print(response.text)
    return get_wiki_summary()

if __name__ == '__main__':
   app.run()