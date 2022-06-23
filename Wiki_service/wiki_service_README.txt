Wikipedia Summary Scraper
Author: David Cornett


contents:  
    wiki_service.py                          
	- standalone flask application 
    wiki_service_requirements.txt
	- flask and wikipedia-related requirements for your virtual env
	

To use it as a service locally, you run it in its own directory 
with its dependencies.  

Steps:
	1) create new virtual environment so you don't need to download dependencies globally - to do this,
	   create a separate directory for this service, then: 
		- pip3 install virtualenv
		- python3 -m venv ./venv
		- source ./venv/bin/activate
	   WARNING:  when done, type 'deactivate' into terminal to leave virtual env
	2) add wiki_service_requirements.txt to this directory
	3) install dependencies:
		- pip3 install -r wiki_service_requirements.txt
	3) add wiki_service.py to your dir and run it: python3 wiki_service.py
	
Now, you can send GET requests with a URL parameter for the attraction you wish to look up.

To send GET requests, add this to your main app.py file:
 
    def get_wiki_summary(attraction: str):
        """
        Returns JSON containing wikipedia summary test for your desired attraction OR message indicating summary can't be found
        Takes any string - process_string() ensures title case and blank spaces will be processed
        """
        def process_string(string: str) -> str:
            new_string = string.title()  # capitalize all words (some wiki entries are case sensitive)
            return new_string.replace(' ', '_')  # return string with blank spaces replaced with underscores
        attraction = process_string(attraction)  # process attraction's name to work with wikipedia search

        # gets JSON containing wikipedia summary for URL parameter
        response = requests.get('http://127.0.0.1:9999/'+attraction)
        wiki_summary = response.json()
        return wiki_summary

You can call this function for whatever attraction you wish.
Finally, run your main app.py file from another terminal window.

You can also print(wiki_summary) for testing purposes.

Let me know if you have any questions!