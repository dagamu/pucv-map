import pygame
from utils import sum_tuples

class PhoneMenu:
    def __init__(self, scene_manager):
        self.scene_name = "Phone Menu"
        
        self.event_handler = EventHandler(self)
        self.btn_rect = pygame.Rect(190, 165, 50, 50)
        self.open_animation_rect = self.btn_rect.scale_by(0.4)
        self.open_animation_target = pygame.Rect( 50, 34, 296, 606 )
        
        self.show_anim_rect = False
        self.scene_manager = scene_manager
    
    def setup(self, asset_manager, animator):
        self.asset_manager = asset_manager
        self.animator = animator
    
    def loop(self, screen):
        phone_bg = self.asset_manager.get("phone_bg")
        screen.blit(phone_bg, (0, 0))
        
        #pygame.draw.rect( screen, "green", self.open_animation_rect, width=3 )
        if self.show_anim_rect:
            pygame.draw.rect( screen, (21, 141, 201), self.open_animation_rect)
                
    def change_scene(self):
        self.scene_manager.next_scene()
            
        
class EventHandler:
    def __init__(self, scene):
        self.scene = scene
        
    def handle_event(self, e, mouse_offset=pygame.Vector2(0,0)):
        if e.type == pygame.MOUSEBUTTONUP:
            self.handle_click(mouse_offset)
        
    def handle_click(self, mouse_offset):
        pos = pygame.mouse.get_pos() - mouse_offset
        if self.scene.btn_rect.collidepoint(pos):
            self.scene.animator.reach_rect(
                lambda: self.scene.open_animation_rect,
                lambda rect: self.scene.open_animation_rect.update(rect),
                self.scene.open_animation_target,
                self.scene.change_scene,
                20
            )
            self.scene.show_anim_rect = True