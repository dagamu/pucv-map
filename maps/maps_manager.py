from maps.main_map import MAIN_MAP
from maps.ING_AU_map import ING_AU_MAP

class MapsManager:
    def __init__(self):
        self.maps = {
            "Main": MAIN_MAP,
            "ING-AU": ING_AU_MAP
        }
    
    def get(self, name):
        return self.maps[name]