# BeerMapr
This webapp uses a micro-services architecture to show information about breweries in a particular geographical location.  

    Features:
    - Users can choose to search for breweries by any zip code, or by clicking 'press for location' to get breweries local to them
    - Users can optionally limit the brewery responses by range around the input location, but to 30 miles (note: a max of 20 breweries will return)
    - Users can optionally filter the responses by brewery type (microbrewery, brewpub, regional brewery)
    - Front page shows image and text of a particular beer style, changing upon each reload
    - Results page reminds user of their input search parameters
    - Results page displays table containing brewery name, type, distance between brewery and input location (in miles), URL (if applicable), wikipedia summary (if applicable)


    Micro-services:
    1) openbrewerydb API: returns data on breweries for a given zip code
        source: https://www.openbrewerydb.org/
    2) Gimme-a-beer: randomly generates image and text about a beer style from multiple options
        source: process ran locally, developed by Robert Baucus, Oregon State University
        For more info, review gimme-a-beer/readme
    3) Wikipedia scraper: gets summary text at the top of a wiki page for a brewery, if the page exists/
        source: process ran locally, developed by David Cornett, Oregon State University
        For more info, review Wiki_service/readme