import pygame
from scenes.map_events import EventHandler

class MapView:
    def __init__(self, scene_manager):
        self.scene_name = "Map View"
        
        self.event_handler = EventHandler(self)
        self.scene_manager = scene_manager
        
        self.map_pos = pygame.Vector2(-200, -300)
        self.window_center = pygame.Vector2( 175, 344 )
        self.target_point = self.window_center.copy() - self.map_pos
        self.move_vel = 7
        
        self.chat_btn = [ ["white", (280, 620), 30 ],
                         [ (21, 141, 201), (280, 620), 28 ] ]
        
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
        
        self.map_image = self.asset_manager.get("proto_map")
        self.mask = self.asset_manager.get("mask")
        
        self.map_size = pygame.Vector2( self.map_image.get_width(), self.map_image.get_height())
        self.original_map_size = self.map_size.copy()
        self.zoom = 1
        
    def loop(self, screen):
        
        pygame.draw.rect( screen, (7, 8, 12), (0,0,360,700))
        screen.blit(self.map_image, (self.map_pos.x, self.map_pos.y))
        
        pygame.draw.circle( screen, *self.chat_btn[0] )
        pygame.draw.circle( screen, *self.chat_btn[1] )
        
        self.event_handler.check_loop()
            
    def update_scale(self):
        self.map_size.scale_to_length( self.original_map_size.length() * self.zoom)
        self.map_image = pygame.transform.scale( self.asset_manager.get("proto_map"), (self.map_size.x, self.map_size.y) )
        self.map_pos = self.window_center - self.target_point * self.zoom
        
