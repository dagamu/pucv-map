import pygame

from utils import alpha_gradient, sum_tuples

class BuildingInfoBox:
    def __init__( self, scene ):
        self.scene = scene
        self.box_render = pygame.Surface( (0,0) )
        
        self.shadow_height = 6
        self.y_vel = 8
        self.icons_topleft = pygame.Vector2(50, 65)
        
        
    def load( self ):
        w, h = self.scene.window_size
        self.pos = pygame.Vector2( 0, h )
        self.box_height = int( h/4 )
        self.box_y_target = h * 3/4
        
        self.font = self.scene.asset_manager.font
        self.big_font = self.scene.asset_manager.big_font
        
        self.shadow = self.render_shadow()
        
    def render_shadow(self):
        shadow_size = ( self.scene.window_size[0], self.shadow_height )
        shadow = pygame.Surface( shadow_size, pygame.SRCALPHA )
        shadow.fill(0)
        shadow = alpha_gradient(shadow, lambda x,y: y*10)
        return shadow
        
    def loop( self, screen ):
        screen.blit( self.shadow, self.pos - pygame.Vector2(0, self.shadow_height))
        screen.blit( self.box_render, self.pos )
        if self.pos[1] > self.box_y_target:
            self.pos += pygame.Vector2(0, -self.y_vel )
            
    def draw_titles(self, box, surf):
        if not "labels" in box.keys():
            return
        title_opt = [ box["name"], True, "white" ]
        title = self.big_font.render( *title_opt )
        surf.blit( title, (50, 20) )
        
        if "long" in box["labels"].keys():
            subtitle_opt = [ box["labels"]["long"], True, "gray" ]
            subtitle = self.font.render( *subtitle_opt )
            surf.blit( subtitle, (50, 42) )
        
    def draw_photo( self, box, surf ):        
        img = self.scene.asset_manager.get( f"{ box['name'] }-photo")
        if not img is None:
            img_w, img_h = img.get_size()
            new_w = img_w * self.box_height / img_h
            img = pygame.transform.scale( img, (new_w, self.box_height) )
            x_offset = box["info-img-offset"]
            img = alpha_gradient(img, lambda x, y: int( (x - x_offset + 180)*1.4) )
            surf.blit( img, ( self.scene.window_size[0] - x_offset, 0 ) )
            
    def draw_icons( self, box, surf ):
        if not "icons" in box.keys():
            return
        icons_pos = self.icons_topleft.copy()
        
        for icon in box["icons"]:
            icon_img = self.scene.asset_manager.get_icon( icon, (20,20) )
            icon_box = pygame.Rect( icons_pos, (30, 30))
            
            pygame.draw.rect(surf, (12, 22, 36), icon_box )
            surf.blit( icon_img, sum_tuples(icons_pos, (4,4)) )

            icons_pos += pygame.Vector2(35,0)
        
    def render( self ):
        w, h = self.scene.window_size
        box_h = self.box_height
        
        s = pygame.Surface( (w, box_h)  )
        s.fill( (20, 30, 45) )
        
        box = self.scene.box_selected
        
        if not set(["icons", "labels"]).issubset( box.keys( )):
            self.scene.box_selected = False
            return
        
        self.draw_titles( box, s )
        self.draw_photo( box, s )
        self.draw_icons( box, s)
        
        self.box_render = s