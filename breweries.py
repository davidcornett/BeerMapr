# does stuff

class Brewery:
    def __init__(self, name: str, type: str, loc: object):
        self.name =  name
        self.type = type
        self.location = loc
    
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type
    
    def get_location(self):
        return self.location

