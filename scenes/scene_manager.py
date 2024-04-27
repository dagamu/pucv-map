from scenes.phone_menu import PhoneMenu
from scenes.app_menu import AppMenu
from scenes.map_view import MapView
from scenes.chat import ChatScene

class SceneManager:
    def __init__(self, asset_manager, scene_number):
        self.scenes = [ PhoneMenu(self), AppMenu(self), MapView(self), ChatScene(self) ]
        self.asset_manager = asset_manager
        
        self.first_scene = scene_number
        self.current_index = self.first_scene   
        self.current_scene = self.scenes[ self.current_index ]
    
    def set_scenes(self):
        for s in self.scenes:
            s.setup(self.asset_manager)
    
    def next_scene(self):
        self.current_index += 1
        self.current_scene = self.scenes[self.current_index]
        
    def loop_of(self, scene_name, screen):
        for s in self.scenes:
            if s.scene_name == scene_name:
                s.loop(screen)
                
    def go_to(self, scene_name):
        for i, s in enumerate(self.scenes):
                if s.scene_name == scene_name:
                    self.current_index = i
                    self.current_scene = s