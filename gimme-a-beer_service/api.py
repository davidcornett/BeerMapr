from flask import Flask
from flask_restful import Resource, Api
from gimme_a_beer_image import gimme_a_beer_image
from gimme_a_beer_description import gimme_a_beer_description
import os, random

'''
{
    "beer_image": [
        "amber_lager",
        "<a href=\"https://imgbb.com/\"><img src=\"https://i.ibb.co/vJtJ63f/american-amber-lager.jpg\" alt=\"american-amber-lager\" border=\"0\" /></a>"
    ],
    "beer_description": [
        "amber_lager",
        "A widely available, sessionable craft beer style that\n        showcases both malt and hops. Amber lagers are a medium-bodied\n         lager with a toasty or caramel-like malt character.\n         Hop bitterness can range from very low to medium-high.\n         Brewers may use decoction mash and dry-hopping to achieve advanced flavors.\n        Category: Dark Lagers\n        Pale\n        Dark 6-14 SRM (Color)\n        Low\n        High 18-30 IBU (Bitterness)\n        Low\n        High 4.8-5.4% ABV (Alcohol)\n        Food Pairings\n\n            Grilled Meats and Vegetables\n            White Cheddar\n            Fruit Desserts\n\n        Glassware & Serving Temperature\n\n        Tulip\n        45-50 \u252c\u2591F\n        Commercial Examples Commercial Examples\n\n            Sam Adams Boston Lager, Boston Beer Co.\n            Lager, Brooklyn Brewery\n            Lighter Than I Look, Figueroa Mountain Brewing\n        "
    ]
}
'''
 
app = Flask(__name__)
api = Api(app)

class GimmeABeer(Resource):
    def get(self):
    
        index = random.randint(1,16)
        beer_image = gimme_a_beer_image(index)
        beer_description = gimme_a_beer_description(index)
        return {'beer_image': beer_image, 'beer_description': beer_description}

api.add_resource(GimmeABeer, '/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 42001)) 
    app.run(port=port, debug=True)