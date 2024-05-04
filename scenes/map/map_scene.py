import pygame
import pygame.draw

from scenes.map.map_events import EventHandler
from scenes.map.map_ui import MapUI

from maps.maps_manager import MapsManager
from utils import scale_tuple

class MapView:
    def __init__(self, scene_manager):
        self.scene_name = "Map View"
        
        self.event_handler = EventHandler(self)
        self.ui = MapUI(self)
        self.maps_manager = MapsManager(self)
        self.scene_manager = scene_manager
        
        self.original_map = self.maps_manager.get("Main")
        self.map = self.original_map
        
        
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
        self.set_viewport()
        self.maps_manager.load()
        self.ui.load()
        self.box_selected = False
        
    def set_viewport(self):
        self.window_size = pygame.Vector2( pygame.display.get_surface().get_size() )
        self.window_center = self.window_size * 0.5
        self.target_point = self.window_center - ( self.map.pos )
        
    def loop(self, screen):
        
        bg_color = self.map.opt["background-color"]
        pygame.draw.rect( screen, bg_color, (0,0,360,700) )
        
        screen.blit(self.map.render, self.map.pos )
        #pygame.draw.circle( screen, "blue", self.target_point * self.map.zoom + self.map.pos, 5)
        
        viewport_size = self.window_size * .9
        viewport_pos = self.target_point * self.map.zoom + self.map.pos - viewport_size * 0.5
        viewport_rect = pygame.Rect([viewport_pos, viewport_size])
        #pygame.draw.rect( screen, "blue", viewport_rect, width=3)
        
        boundaries_rect = pygame.Rect( self.map.boundaries )
        #boundaries_rect.inflate_ip( scale_tuple( boundaries_rect.size, (1/self.zoom) ) )
        boundaries_rect.update( self.map.pos, scale_tuple( boundaries_rect.size, self.map.zoom ) )
        #pygame.draw.rect( screen, "green", boundaries_rect, width=3)
        
        if not boundaries_rect.contains( viewport_rect ):
            #print("Out")
            pass
        
        w, h = self.window_size
        if self.box_selected:
            self.ui.building_infobox.loop( screen )
        
        self.ui.render( screen )
        self.event_handler.check_loop()
        
    def render_colliders(self, mouse_pos):
        pygame.draw.circle( self.map_render, "red", mouse_pos - self.map.pos, 3 )
        for box in self.map.boxes:
            box_rect = pygame.Rect( box["collider"] )
            box_rect.update( scale_tuple( (*box_rect.topleft, *box_rect.size), self.map.zoom))
            pygame.draw.rect( self.map_render, "red", box_rect, width=3)