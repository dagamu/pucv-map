from maps.main_map import MAIN_MAP
from maps.ING_AU_map import ING_AU_MAP

class MapsManager:
    def __init__(self, scene):
        self.maps = {
            "Main": MAIN_MAP,
            "ING-AU": ING_AU_MAP
        }
        self.scene = scene
        
    def load( self ):
        for m in self.maps.values():
            m.setup()
            m.set_scene( self.scene )
            m.load( self.scene.asset_manager )
    
    def get(self, name):
        self.maps[name].setup()
        return self.maps[name]