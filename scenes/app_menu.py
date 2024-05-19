import pygame

class AppMenu:
    def __init__(self, scene_manager):
        self.scene_name = "App Menu"
        
        self.event_handler = EventHandler(self)
        self.scene_manager = scene_manager
        self.frame_count = 0
        
    def setup(self, asset_manager, animator):
        self.asset_manager = asset_manager
        self.animator = animator
    
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
        
    def handle_event(self, e, mouse_offset=pygame.Vector2(0,0)):
        if e.type == pygame.MOUSEBUTTONUP:
            self.handle_click(mouse_offset)
        
    def handle_click(self, mouse_offset):
        pos = pygame.mouse.get_pos() - mouse_offset
        if 232 <= pos[0] <= 360 and 480 <= pos[1] <= 550:
            self.scene.scene_manager.next_scene()