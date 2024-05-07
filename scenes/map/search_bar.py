import pygame

from utils import sign
from textbox import TextBox

class SearchBar:
    def __init__(self, scene):
        self.scene = scene
        self.focus = False
        self.text_bar = { "text": "" }
        
        
        self.color = (0,0,0,120)
        
    def load( self ):
        self.font = self.scene.asset_manager.font
        self.text_box = TextBox( self.font )
        
        w, h = self.scene.window_size
        self.size = pygame.Vector2( w*0.45, 25)
        self.pos = pygame.Vector2( w/2 - self.size.x/2, 70 )
        self.rect = pygame.Rect( self.pos, self.size )
        self.render = pygame.Surface( self.size, pygame.SRCALPHA )
        
        self.focus_size = pygame.Vector2( w*0.7, 50)
        self.focus_pos = pygame.Vector2( w/2 - self.focus_size.x/2, 110 )
        self.focus_anim_vel = 0.1
        self.focus_status = 0
        
        self.unfocus_size = self.size.copy()
        self.unfocus_pos = self.pos.copy()
        
        self.icon_height = self.size.y*.6
        self.icon = self.scene.asset_manager.get_icon("search", ( self.icon_height*.8, self.icon_height*.8 ))
        self.go_to_icon = self.scene.asset_manager.get_icon("go_to", ( self.icon_height, self.icon_height ))
        
        self.draw()
        
        
    def draw(self):
        self.render = pygame.Surface( self.size, pygame.SRCALPHA )
        pygame.draw.circle( self.render, self.color, (self.size.y/2, self.size.y/2), self.size.y/2 )
        rect_size = ( self.size.x - self.size.y, self.size.y )
        pygame.draw.rect( self.render, self.color, ( (self.size.y/2,0), rect_size )  )
        pygame.draw.circle( self.render, self.color, ( self.size.x - self.size.y/2, self.size.y/2), self.size.y/2 )
        
        self.render.blit( self.icon, (10, (self.size.y - self.icon_height)/2 ))
        if "render" in self.text_bar.keys():
            text_height = self.text_bar["render"].get_size()[1]
            text_bar_pos = (40, (self.size.y - text_height) / 2)
            self.render.blit( self.text_bar["render"], text_bar_pos )
            
        if self.text_bar["text"] in self.scene.maps_manager.target_nodes.keys():
            self.render.blit( self.go_to_icon, (self.size.x - 30, (self.size.y - self.icon_height)/2 ))
    
    def loop(self, screen ):
        self.draw()
        if self.focus_status != int( self.focus ):
            self.focus_anim()
        screen.blit( self.render, self.pos ) 
        
    def focus_anim(self):
        self.focus_status += self.focus_anim_vel * -sign(self.focus_status - int( self.focus ))
        if self.focus_status != pygame.math.clamp( self.focus_status, 0, 1 ):
            self.focus_status = int(self.focus)
            return
            
        self.size = self.unfocus_size.lerp( self.focus_size, self.focus_status )
        self.pos = self.unfocus_pos.lerp( self.focus_pos, self.focus_status )
        
    def set_text_bar( self, value ):
        self.text_bar["text"] = value
        self.text_bar["render"] = self.render_text_bar()
        
    def render_text_bar(self):
        return self.text_box.render( self.text_bar["text"], max_box_width=self.size.x*0.7, bg_color=(0,0,0,0) )
        
    def handle_key( self, e ):
        text_is_id = self.text_bar["text"] in self.scene.maps_manager.target_nodes.keys()
        if e.key == pygame.K_BACKSPACE:
            self.set_text_bar( self.text_bar["text"][:-1] ) 
        elif e.key == pygame.K_RETURN and text_is_id :
            self.scene.maps_manager.start_find( self.text_bar["text"] )
        else:
            self.set_text_bar( self.text_bar["text"] + e.unicode )
            
        
        
    def toggle_focus(self):
        self.focus = not self.focus
    