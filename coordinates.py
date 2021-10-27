# does stuff
# attribution: https://pgeocode.readthedocs.io/en/latest/overview.html#quickstart

from os import X_OK
import pgeocode
import json

class Location:
    def __init__(self, zip_code, x_cord=None, y_cord=None):
        if x_cord is None or y_cord is None:  # if we don't already have coordinates, we must look them  up
            self.zip_code = zip_code[:5]  # zip codes must be 5-digit only, slice removes longer zip codes

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


    def calc_distance(comparison_location: object) -> float:
        """
        calculates miles between latitude/longitude coordinates
        Note: this simple implementation assumes a flat plane.  This is accurate enough for the limited range of brewery searches supported by
        beermapr.  Greater search radii will need an implementation taking into account Earth's spherical nature. See 'Great Circle' algorithm.
        """
        return 5

    """
    def get_gps(self, zip_code: str) -> str:
        nomi = pgeocode.Nominatim('US')
        query = nomi.query_postal_code(zip_code).to_json()
        dict = json.loads(query)
        return [str(dict['longitude']), str(dict['latitude'])]
    """
