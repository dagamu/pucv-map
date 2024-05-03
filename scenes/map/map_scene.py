import pygame

from scenes.map.map_events import EventHandler
from scenes.map.map_ui import MapUI

from maps.maps_manager import MapsManager
from utils import scale_tuple, sum_tuples, alpha_gradient

class MapView:
    def __init__(self, scene_manager):
        self.scene_name = "Map View"
        
        self.event_handler = EventHandler(self)
        self.ui = MapUI(self)
        self.maps_manager = MapsManager()
        self.scene_manager = scene_manager
    
        self.map_pos = pygame.Vector2(-100, -100)
        self.move_vel = 7
        
        self.chat_btn = [ ["white", (280, 620), 30 ],
                         [ (21, 141, 201), (280, 620), 28 ] ]
        
        self.original_map = self.maps_manager.get("Main")
        self.current_map = self.original_map
        
        
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
        font = self.asset_manager.font
        
        self.ui.load()
        
        self.window_size = pygame.Vector2( pygame.display.get_surface().get_size() )
        self.window_center = self.window_size * 0.5
        self.target_point = self.window_center.copy() - self.map_pos
        
        self.box_selected = False
        self.building_info_pos = pygame.Vector2( 0, self.window_size[1] )
        self.building_info_vel = 8
        self.building_info_target = self.window_size[1] * 3/4
        
        self.map_render = self.current_map.render(font, 1, self.box_selected)
        self.mask = self.asset_manager.get("mask")
        
        self.map_size = pygame.Vector2( self.map_render.get_width(), self.map_render.get_height())
        self.original_map_size = self.map_size.copy()
        self.current_map.load( asset_manager )
        
        self.zoom = 1
        self.zoomClamp = ( 0.75, 2 )
        
        self.update_scale()
        
    def loop(self, screen):
        
        bg_color = self.current_map.opt["background-color"]
        pygame.draw.rect( screen, bg_color, (0,0,360,700))
        mouse_pos = pygame.Vector2( pygame.mouse.get_pos() )
        
        screen.blit(self.map_render, (self.map_pos.x, self.map_pos.y))
        
        w, h = self.window_size
        if self.box_selected:
            shadow_height = 6
            shadow = pygame.Surface( (w, shadow_height), pygame.SRCALPHA )
            shadow.fill(0)
            shadow = alpha_gradient(shadow, lambda x,y: y*10)
            screen.blit( shadow, self.building_info_pos - pygame.Vector2(0, shadow_height))
            screen.blit( self.building_info_render, self.building_info_pos )
            if self.building_info_pos[1] > self.building_info_target:
                self.building_info_pos += pygame.Vector2(0, -self.building_info_vel )
            
        pygame.draw.circle( screen, *self.chat_btn[0] )
        pygame.draw.circle( screen, *self.chat_btn[1] )
        
        self.ui.render( screen )
            
        self.event_handler.check_loop()
        
    def render_colliders(self, screen, mouse_pos):
        pygame.draw.circle( self.map_render, "red", mouse_pos - self.map_pos, 3 )
        for box in self.current_map.boxes:
            box_rect = pygame.Rect( box["collider"] )
            box_rect.update( scale_tuple( (*box_rect.topleft, *box_rect.size), self.zoom))
            pygame.draw.rect( self.map_render, "red", box_rect, width=3)
        
        
    def render_building_info(self):
        
        w, h = self.window_size
        box_height = int(h/4)
        s = pygame.Surface( (w, box_height)  )
        s.fill( (20, 30, 45) )
        
        box = self.box_selected
        
        title_opt = [ box["name"], True, "white" ]
        title = self.asset_manager.big_font.render( *title_opt )
        
        subtitle_opt = [ box["labels"]["long"], True, "gray" ]
        subtitle = self.asset_manager.font.render( *subtitle_opt )
        
        img = self.asset_manager.get( f"{ box['name'] }-photo")
        if not img is None:
            img_w, img_h = img.get_size()
            new_w = img_w *  box_height / img_h
            img = pygame.transform.scale( img, (new_w, box_height) )
            x_offset = box["info-img-offset"]
            img = alpha_gradient(img, lambda x, y: int( (x - x_offset + 180)*1.4) )
            s.blit( img, ( w - x_offset, 0 ) )
        
        s.blit( title, (50, 20) )
        s.blit( subtitle, (50, 42) )
        
        icons_topleft = pygame.Vector2(50, 65)
        icons_pos = icons_topleft.copy()
        
        for icon in box["icons"]:
            
            icon_img = self.asset_manager.get_icon( icon, (20,20) )
            icon_box = pygame.Rect( icons_pos, (30, 30))
            
            pygame.draw.rect(s, (12, 22, 36), icon_box )
            s.blit( icon_img, sum_tuples(icons_pos, (4,4)) )

            icons_pos += pygame.Vector2(35,0)
        
        self.building_info_render = s
            
    def update_scale(self):
        
        self.zoom = pygame.math.clamp( self.zoom, *self.zoomClamp )
        
        self.map_size.scale_to_length( self.original_map_size.length() * self.zoom)
        font = self.asset_manager.font
        self.map_render = pygame.transform.scale( self.current_map.render( font, self.zoom, self.box_selected ), (self.map_size.x, self.map_size.y))
        self.map_pos = self.window_center - self.target_point * self.zoom
        
