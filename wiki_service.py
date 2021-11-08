from flask import Flask, request
import os
import requests
import wikipedia
import json

app = Flask(__name__)

# Routes 
@app.route('/<attraction>')
def root(attraction: str) -> object:
    """
    Returns json object containing either the wikipedia summary paragraph for the attraction arg or a message that no summary can be found
    """
    
    def process_string(string: str) -> str:
        new_string = string.title()  # capitalize all words (some wiki entries are case sensitive)
        return new_string.replace(' ', '_')  # return string with blank spaces replaced with underscores
    
    attraction = process_string(attraction)  # process attraction's name to work with wikipedia search

    try:
        blurb = wikipedia.summary(attraction, 0, 0, False)
    except:
        blurb = 'No wikipedia summary available'
    
    return {'summary': blurb}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 9999)) 
    app.run(port=port, debug=True)