from scenes.app_menu import EventHandler
import pygame

class MapView:
    def __init__(self, scene_manager):
        self.event_handler = EventHandler(self)
        self.scene_manager = scene_manager
        
        self.map_pos = pygame.Vector2()
        self.move_vel = 7
        self.dragging = False
        self.prev_mouse_pos = pygame.Vector2()
        
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
        
        self.map_image = self.asset_manager.get("proto_map")
        self.mask = self.asset_manager.get("mask")
        
        self.map_size = pygame.Vector2( self.map_image.get_width(), self.map_image.get_height())
        self.original_map_size = self.map_size.copy()
        self.zoom = 1
        
    def loop(self, screen):
        
        
        surf = self.mask.copy()
        surf.blit(self.map_image, (self.map_pos.x, self.map_pos.y), None, pygame.BLEND_RGBA_MULT)
        pygame.draw.rect( surf, "blue", (
            175 * self.zoom + self.map_pos.x,
            344 * self.zoom + self.map_pos.y,
            10, 10))
        
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.Vector2( pygame.mouse.get_pos() )
            if self.dragging:
                self.map_pos += mouse_pos - self.prev_mouse_pos
            else:
                self.dragging = True
            self.prev_mouse_pos = mouse_pos
        else:
            self.dragging = False
            
        
        screen.blit(surf, (0, 0))
        pygame.draw.rect( screen, "red", (175, 344, 10, 10))
        
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
            #self.map_pos = self.map_pos - pygame.Vector2( 0.01*self.original_map_size.x, 0.01*self.original_map_size.y ) * 0.5
            self.zoom += 0.01
            self.update_scale()
            
        if keys[pygame.K_x]:
            #self.map_pos += pygame.Vector2( 0.01*self.map_size.x, 0.01*self.map_size.y )
            self.zoom -= 0.01
            self.update_scale()
            
    def update_scale(self):
        self.map_size.scale_to_length( self.original_map_size.length() * self.zoom)
        self.map_image = pygame.transform.scale(self.asset_manager.get("proto_map"), (self.map_size.x, self.map_size.y))
        
