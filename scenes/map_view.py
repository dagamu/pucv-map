from scenes.app_menu import EventHandler
import pygame

class MapView:
    def __init__(self, scene_manager):
        self.event_handler = EventHandler(self)
        self.scene_manager = scene_manager
        
        self.map_pos = pygame.Vector2()
        self.move_vel = 7
        
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
        
        self.map_image = self.asset_manager.get("proto_map")
        self.mask = self.asset_manager.get("mask")
        self.map_size = pygame.Vector2( self.map_image.get_width(), self.map_image.get_height())
        
    def loop(self, screen):
        
        
        surf = self.mask.copy()
        surf.blit(self.map_image, (self.map_pos.x, self.map_pos.y), None, pygame.BLEND_RGBA_MULT)
        
        screen.blit(surf, (0, 0))
        
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]: 
            self.map_pos.x += self.move_vel
            
        if keys[pygame.K_RIGHT]: 
            self.map_pos.x -= self.move_vel
              
        if keys[pygame.K_UP]: 
            self.map_pos.y += self.move_vel
               
        if keys[pygame.K_DOWN]:
            self.map_pos.y -= self.move_vel 
            
        if keys[pygame.K_z]:
            self.map_size.scale_to_length( 
                                    self.map_size.length() * 1.01)
            self.map_image = pygame.transform.scale(self.asset_manager.get("proto_map"), (self.map_size.x, self.map_size.y))
        if keys[pygame.K_x]:
            self.map_size.scale_to_length( 
                                    self.map_size.length() *0.99)
            self.map_image = pygame.transform.scale(self.asset_manager.get("proto_map"), (self.map_size.x, self.map_size.y))
        