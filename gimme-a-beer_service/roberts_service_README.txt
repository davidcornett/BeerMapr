TEAM UNICORN CONFIDENTIAL INFORMATION

robert's beer description / beer image API readme

contents:  
    api.py                          
	- standalone flask-restful application 
	
	gimme_a_beer_description.py     
	- imported into api.py,  returns the description string
	
	gimme_a_beer_image.py           
	- imported into api.py,  
	  returns the URL string for the image 
	  (hosted on https://lkilgoretrout.imgbb.com/)
	

To use it as a service, you simply run it in its own directory 
with its dependencies ( both gimme_a_beer.py files)
and then you send it GET requests like so ( or however you want to do it)

	def gimme_a_beer():
		response = requests.get('http://127.0.0.1:42001')  # you change the port number at the bottom of api.py
		beer = response.json()
		return beer


if you print(beer) you will get a JSON formatted string with one of 16 possible values:
for example:
    
	{
		"beer_image": [
			"amber_lager",
			"<a href=\"https://imgbb.com/\"><img src=\"https://i.ibb.co/vJtJ63f/american-amber-lager.jpg\" alt=\"american-amber-lager\" border=\"0\" /></a>"
		],
		"beer_description": [
			"amber_lager",
			"A widely available, sessionable craft beer style that\nshowcases both malt and hops. Amber lagers are a medium-bodied\n         lager with a toasty or caramel-like malt character.\n         Hop bitterness can range from very low to medium-high.\n         Brewers may use decoction mash and dry-hopping to achieve advanced flavors.\n        Category: Dark Lagers\n        Pale\n        Dark 6-14 SRM (Color)\n        Low\n        High 18-30 IBU (Bitterness)\n        Low\n        High 4.8-5.4% ABV (Alcohol)\n        Food Pairings\n\n            Grilled Meats and Vegetables\n            White Cheddar\n            Fruit Desserts\n\n        Glassware & Serving Temperature\n\n        Tulip\n        45-50 \u252c\u2591F\n        Commercial Examples Commercial Examples\n\n            Sam Adams Boston Lager, Boston Beer Co.\n            Lager, Brooklyn Brewery\n            Lighter Than I Look, Figueroa Mountain Brewing\n        "
		]
	}

beer["beer_image"] to access an HTML <img> tag string that can be plugged right
 into your page to show a picture of 'amber_lager' (in this case)

beer["beer_description"][1] gives you the description string for the same beer. You may need to run a little 
CSS on the string to get it how you like it because I used triple-quoted-strings and they don't translate well
with spaces and newlines.

Any questions hit me up !

GO UNICORNS!