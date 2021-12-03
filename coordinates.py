# Location objects hold zip code and gps coords, and method for calculating distance
# attribution: https://pgeocode.readthedocs.io/en/latest/overview.html#quickstart

from os import X_OK
import pgeocode
import json
from haversine import haversine, Unit

class Location:
    def __init__(self, zip_code, x_coord=None, y_coord=None):
        self.zip_code = zip_code[:5]  # zip codes must be 5-digit only, slice removes longer zip codes
        self.is_valid = True

        # Location needs either zip code or coords
        if self.zip_code == '' and (x_coord is None or y_coord is None):
            self.is_valid = False

        if x_coord is None or y_coord is None:  # if we don't already have coordinates, we must look them up
            # get coordinates data via pgeocode library
            nomi = pgeocode.Nominatim('US')
            query = nomi.query_postal_code(self.zip_code).to_json()
            location_dict = json.loads(query)

            # set lat/long coordinates
            self.x = str(location_dict['longitude'])
            self.y = str(location_dict['latitude'])
        else:
            self.x = x_coord
            self.y = y_coord

    def process_x(self, x: str) -> str:
        output = ''
        switch = False
        for char in x:
            if char == ',':
                switch = True
            else:
                if switch is True:
                    output += char
        return output

    def process_y(self, y: str) -> str:
        output = ''
        for char in y:
            if char == ',':
                return output
            output += char

    def get_x(self) -> str:
        # longitude
        return self.x 
    
    def get_y(self) -> str:
        # latitude
        return self.y

    def get_zip(self) -> str:
        return self.zip_code

    def calc_distance(self, comparison_location: object) -> float:
        """
        calculates miles between latitude/longitude coordinates 
        Must revieve another location object as parameter
        """
        loc1 = (float(comparison_location.get_y()), float(comparison_location.get_x()))
        loc2 = (float(self.get_y()), float(self.get_x()))
        return haversine(loc1, loc2, unit=Unit.MILES)
    
    def get_is_valid(self) -> bool:
        return self.is_valid

