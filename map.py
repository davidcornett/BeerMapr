# Map objects hold all other objects in the program, including user locations and breweries.
import wikipedia

class Map:
    def __init__(self, user_location, range):
        self.user_location = user_location  # holds location object of user
        self.brewery_list = []  # holds  brewery objects processed from  OpenBreweryDB - removes need to re-query if user tweaks range/filter
        self.selected_breweries = []   # holds BY DISTANCE list of brewery objects meeting user's range and filter criteria (if applicable)
        self.max_range = 30
        self.range = self.set_range(range)

    # getter and setter methods for class attributes
    def get_all_breweries(self) -> list:
        return self.brewery_list
    
    def get_selected_breweries(self) -> list:
        return self.selected_breweries
    
    def select_breweries(self) -> None:
        """
        Method should be called after all breweries have been added.
        Creates list of selected breweries and sorts by distance from user
        """
        self.selected_breweries = [brewery for brewery in self.brewery_list if brewery.get_is_selected()]  
        self.selected_breweries.sort(key=lambda brewery:brewery.get_distance())  

    def get_user_location(self) -> list:
        return self.user_location

    def add_brewery(self, brewery) -> None:
        self.brewery_list.append(brewery)

    def set_wiki_summaries(self) -> None:
        """
        Loops through selected breweries, making wikipedia API call to get the summary if available.
        If none available, sets message indicating that.
        """
        for brewery in self.selected_breweries:
            try:
                blurb = wikipedia.summary(brewery.get_name(), 0, 0, False)
                brewery.set_wiki_summary(blurb)
            except:
                brewery.set_wiki_summary('No summary available')

    def set_range(self, range: str) -> int:
        """
        Sets class attribute range
        Convers range parameter from str to int
        Sets range at 30 by defailt if blank
        """
        try:
            range = min(int(range), self.max_range)
        except:
            range = self.max_range
        
        return range
    
    def get_range(self) -> int:
        return self.range
    

