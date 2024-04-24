import pygame

class AppMenu:
    def __init__(self, scene_manager):
        self.event_handler = EventHandler(self)
        self.scene_manager = scene_manager
        self.frame_count = 0
        
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
    
    def loop(self, screen):
        self.frame_count += 1
        
        if self.frame_count <= 70:
            bg_image = self.asset_manager.get("app_loading")
        else:
            bg_image = self.asset_manager.get("app_menu")
            
        screen.blit(bg_image, (0, 0))
        
class EventHandler:
    def __init__(self, scene):
        self.scene = scene
        
    def handle_click(self):
        pos = pygame.mouse.get_pos()
        if 165 <= pos[0] <= 225 and 340 <= pos[1] <= 390:
            self.scene.scene_manager.next_scene()