# does stuff
import wikipedia

class Map:
    def __init__(self, user_location):
        self.user_location = user_location  # holds location object of user
        self.brewery_list = []  # holds  brewery objects processed from  OpenBreweryDB - removes need to re-query if user tweaks range/filter
        self.selected_breweries = []   # holds BY DISTANCE list of brewery objects meeting user's range and filter criteria (if applicable)

    def get_all_breweries(self) -> list:
        return self.brewery_list
    
    def get_selected_breweries(self) -> list:
        return self.selected_breweries
    
    def select_breweries(self):
        self.selected_breweries = [brewery for brewery in self.brewery_list if brewery.get_is_selected()]  # create list of selected breweries
        self.selected_breweries.sort(key=lambda brewery:brewery.get_distance())  # sort selected breweries by distance from user

    def get_user_location(self) -> list:
        return self.user_location

    def add_brewery(self, brewery):
        self.brewery_list.append(brewery)

    def set_wiki_summaries(self):
        for brewery in self.selected_breweries:
            try:
                blurb = wikipedia.summary(brewery.get_name(), 0, 0, False)
                brewery.set_wiki_summary(blurb)
            except:
                brewery.set_wiki_summary('No summary available')



