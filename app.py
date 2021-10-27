from flask import Flask, request
import os
import requests
from coordinates import Location
from breweries import Brewery
import json

import pgeocode

from flask.templating import render_template
app = Flask(__name__)

# Routes 

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        zip_code = request.form['zip']
        range = request.form['range']
        filter = request.form['breweryType']

        # create user location that has latitude/longitude
        user_location = Location(zip_code)
  
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

        brewery_list = [] # list of brewery objects
        for brewery in breweries:
            brewer_location = Location(brewery['postal_code'], brewery['longitude'], brewery['latitude'])
            new_brewery = Brewery(brewery['name'], brewery['brewery_type'], brewer_location)
            brewery_list.append(new_brewery)
            #print(brewery['name'])
            
        #print(response.text)

        for b in brewery_list:
            print(b.get_name() + str(b.get_location().get_x()) + ', ' + str(b.get_location().get_y()))
            print(user_location.get_x() + ', ' + str(user_location.get_y()))
        """
        test = ''
        for brewery in brewery_list:
            #test += brewery[0]
            test += brewery.get_name()
            test += ', '
            test += brewery.get_location().get_x()
            test += '; '
        """

        

        return 'dum'
    
    else:
        return render_template("home.html")

@app.route('/results')
def get_results():
    pass
    

@app.route('/test')
def test():

    #response = requests.get('https://api.github.com')
    #response = requests.get('https://api.openbrewerydb.org/breweries?by_dist=38.87418813900499,-77.30317040648194&per_page=50')
    #response = requests.get('https://api.openbrewerydb.org/breweries/12432')
    #print(response.text)
    return "t"

if __name__ == '__main__':
   app.run()