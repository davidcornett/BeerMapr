# Brewery Objects hold all brewery-specific information, including Location object

class Brewery:
    def __init__(self, name: str, type: str, loc: object, url: str):
        self.name =  name
        self.type = type
        self.url = url
        self.location = loc
        self.in_range = None 
        self.distance_from_user = None
        self.is_selected = False
        self.wiki_summary = None
    
    # getter and setter methods for Brewery attributes
    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.type

    def get_url(self) -> str:
        return self.url
    
    def get_location(self) -> object:
        return self.location

    def set_in_range(self, range_bool: bool) -> None:
        self.in_range = range_bool
        
    def set_distance(self, distance: float) -> None:
        self.distance_from_user = distance

    def get_distance(self) -> float:
        return self.distance_from_user

    def get_is_selected(self) -> bool:
        return self.is_selected

    def select(self) -> None:
        self.is_selected = True

    def set_wiki_summary(self, blurb: str) -> None:
        self.wiki_summary = blurb

    def get_wiki_summary(self) -> str:
        return self.wiki_summary