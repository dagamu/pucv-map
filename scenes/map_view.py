from scenes.app_menu import EventHandler

class MapView:
    def __init__(self, scene_manager):
        self.event_handler = EventHandler(self)
        self.scene_manager = scene_manager
        
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
        
    def loop(self, screen):
        bg_image = self.asset_manager.get("proto_map")
        screen.blit(bg_image, (0, 0))