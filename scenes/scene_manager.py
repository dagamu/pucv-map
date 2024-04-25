from scenes.phone_menu import PhoneMenu
from scenes.app_menu import AppMenu
from scenes.map_view import MapView

class SceneManager:
    def __init__(self, asset_manager):
        self.scenes = [ PhoneMenu(self), AppMenu(self), MapView(self) ]
        self.asset_manager = asset_manager
        
        self.current_scene = self.scenes[0]
        self.current_index = 0   
    
    def set_scenes(self):
        for s in self.scenes:
            s.setup(self.asset_manager)
    
    def next_scene(self):
        self.current_index += 1
        self.current_scene = self.scenes[self.current_index]