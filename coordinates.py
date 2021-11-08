# does stuff
# attribution: https://pgeocode.readthedocs.io/en/latest/overview.html#quickstart

from os import X_OK
import pgeocode
import json
from haversine import haversine, Unit

class Location:
    def __init__(self, zip_code, x_cord=None, y_cord=None):
        self.zip_code = zip_code[:5]  # zip codes must be 5-digit only, slice removes longer zip codes

        if x_cord is None or y_cord is None:  # if we don't already have coordinates, we must look them  up
            # get coordinates data via pgeocode library
            nomi = pgeocode.Nominatim('US')
            query = nomi.query_postal_code(self.zip_code).to_json()
            location_dict = json.loads(query)

            # set lat/long coordinates
            self.x = str(location_dict['longitude'])
            self.y = str(location_dict['latitude'])
        else:
            self.x = x_cord
            self.y = y_cord


    def get_x(self):
        return self.x 
    
    def get_y(self):
        return self.y

    def get_zip(self):
        return self.zip_code

    def calc_distance(self, comparison_location: object) -> float:
        """
        calculates miles between latitude/longitude coordinates.
        """
        loc1 = (float(comparison_location.get_y()), float(comparison_location.get_x()))
        loc2 = (float(self.get_y()), float(self.get_x()))
        return haversine(loc1, loc2, unit=Unit.MILES)

