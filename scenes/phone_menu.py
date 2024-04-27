import pygame

class PhoneMenu:
    def __init__(self, scene_manager):
        self.scene_name = "Phone Menu"
        
        self.event_handler = EventHandler(self)
        self.open_animation = False
        self.open_animation_rect = ( 205, 125, 20, 20 )
        self.open_animation_target = ( 50, 34, 296, 606 )
        
        self.scene_manager = scene_manager

        self.animation_totalframes = 13
        self.set_animation_vel()
        
    def set_animation_vel(self):
        self.animation_vel = []
        for i, val in enumerate(self.open_animation_rect):
            self.animation_vel.append( (self.open_animation_target[i] - val) / self.animation_totalframes )
        
    def sum_tuples(self, a, b):
        result = []
        for i, val in enumerate(a):
            result.append(val + b[i])
        return result
    
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
    
    def loop(self, screen):
        phone_bg = self.asset_manager.get("phone_bg")
        screen.blit(phone_bg, (0, 0))
        
        if self.open_animation:
            pygame.draw.rect( screen, (21, 141, 201), self.open_animation_rect)
            if self.open_animation_rect[0] >= self.open_animation_target[0]:
                self.open_animation_rect = self.sum_tuples(self.open_animation_rect, self.animation_vel)
            else:
                self.scene_manager.next_scene()
            
        
class EventHandler:
    def __init__(self, scene):
        self.scene = scene
        
    def handle_event(self, e):
        if e.type == pygame.MOUSEBUTTONUP:
            self.handle_click()
        
    def handle_click(self):
        pos = pygame.mouse.get_pos()
        if 190 <= pos[0] <= 240 and 162 <= pos[1] <= 211:
            self.scene.open_animation = True