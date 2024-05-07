import pygame
from math import log10
from scenes.map.map_render import MapRender


default_opt = { 
               "background-color": (7, 8, 12),
               "start-pos": (-200, 0),
               "start-zoom": 1,
               "zoom-clamp": ( 0.75, 2 ),
               "return-action": ["map", "Main"]
            }

class Map:
    def __init__( self, size, background, boxes, lines, green_areas, icons, nodes= [], boundaries=[0,0,300,300 ], opt={} ):
        
        self.background = background
        self.boxes = boxes
        self.lines = lines
        self.green_areas = green_areas
        self.icons = icons
        self.nodes = nodes
        self.boundaries = boundaries
        
        self.opt = { **default_opt, **opt }   
        self.original_size = pygame.Vector2( size )
        
        self.render_manager = MapRender( self )
        
        self.path = []
        
    def setup(self):
        self.size = self.original_size.copy()
        self.pos = pygame.Vector2( self.opt["start-pos"] )
        self.zoom = self.opt["start-zoom"]
        self.zoomClamp = self.opt["zoom-clamp"]
        self.move_vel = 2
        self.zoom_vel = 0.1
        
    def load(self, asset_manager, scale=True):
        self.asset_manager = asset_manager
        self.render = self.render_manager.draw()
        for i in self.icons:
            i["render"] = self.asset_manager.get_icon( i["name"], (24, 24) )
        if scale:
            self.update_scale()
            
    def set_scene( self, scene ):
        self.scene = scene
        
    def set_path( self, path ):
        self.path = path
        self.re_render()
        
    def re_render( self ):
        self.render = pygame.transform.scale( self.render_manager.draw(), self.size )
            
    def update_scale(self):
        self.zoom = pygame.math.clamp( self.zoom, *self.zoomClamp )
        self.size.scale_to_length( self.original_size.length() * self.zoom )
        self.re_render()
        self.pos = self.scene.window_center - self.scene.target_point * self.zoom
        
    def change_zoom(self, change):
        self.zoom += self.zoom**2 * change * self.zoom_vel
        self.update_scale()
        
    def move( self, v ):
        self.pos += v * self.move_vel
        self.scene.target_point += v * self.move_vel / -self.zoom
        
    def get_pos(self):
        return self.pos
        
    def get_zoom(self):
        return self.zoom
    
    
    