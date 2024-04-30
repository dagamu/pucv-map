from maps.main_map import MAIN_MAP

class MapsManager:
    def __init__(self):
        self.maps = {
            "Main": MAIN_MAP
        }
    
    def get(self, name):
        return self.maps[name]