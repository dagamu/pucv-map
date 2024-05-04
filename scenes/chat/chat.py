import pygame
import pygame.display

from scenes.chat.messages_render import MsgRender
from scenes.chat.chat_events import EventHandler
from textbox import TextBox
from utils import scale_tuple, sum_tuples

class ChatScene:
    def __init__(self, scene_manager):
        self.scene_name = "Chat"
        
        self.event_handler = EventHandler(self)
        self.scene_manager = scene_manager
        
        self.show_time = 15
        
        self.frame_count = 0
        self.fade_frame = -1
        
        self.text_bar_focus = True
        self.text_bar_placeholder = "Escribe tu mensaje"
        self.text_bar_msg = { "text": self.text_bar_placeholder }
        
        self.messages = [{ "user": "bot", "text": "Hola! ¿En qué te puedo ayudar?" }]
        
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
        
        self.window_size = pygame.display.get_surface().get_size()
        self.surface = pygame.Surface( self.window_size )
        self.s_pos = pygame.Vector2( self.window_size[0], 0)
        
        self.font = pygame.font.SysFont("Arial", 12)
        self.msg_render = MsgRender(self)
        self.bar_textbox = TextBox( self.font )
        
        pet_img = self.asset_manager.get("pet")
        self.pet_img = pygame.transform.scale( pet_img, (25,25))
        
    
    def loop(self, screen):
        self.frame_count += 1
        w, h = self.window_size
        
        if self.frame_count <= self.show_time:
            self.fade_in_anim( screen, w )
            
        elif self.fade_frame > 0:
            self.fade_out_anim( screen, w )
            
        self.surface.fill("gray10")
        
        pygame.draw.rect( self.surface, "gray15", (0, h - 120, w, 120  )) # BOTTOM BAR
        
        send_box = pygame.Rect( w-90, h - 110, 45, 50)
        pygame.draw.rect( self.surface, "gray10", send_box ) # SEND
        
        send_icon = self.asset_manager.get_icon("send")
        semi_icon_size = scale_tuple(send_icon.get_size(), -0.5)
        icon_pos = sum_tuples( send_box.center, semi_icon_size )
        self.surface.blit( send_icon, icon_pos )
        
        exit_box = pygame.Rect( 50, 50, 40, 40  )
        pygame.draw.rect( self.surface, "gray15", exit_box ) # EXIT
        
        exit_icon = self.asset_manager.get_icon("arrow-left")
        semi_icon_size = scale_tuple( exit_icon.get_size(), -0.5 )
        icon_pos = sum_tuples( exit_box.center, semi_icon_size )
        self.surface.blit( exit_icon, icon_pos )
        
        if not "render" in self.text_bar_msg.keys() or self.text_bar_msg["text-redered"] != self.text_bar_msg["text"]:
            text_box_color = "gray11" if self.text_bar_focus else "gray10"
            self.text_bar_msg["render"] = self.bar_textbox.render( self.text_bar_msg["text"], "left", 10, w - 180, text_box_color, min_width=w-180, max_height=50 )
            self.text_bar_msg["text-redered"] = str( self.text_bar_msg["text"] )
        self.surface.blit( self.text_bar_msg["render"], (80, h - 110) )
        
        self.msg_render.render_mesagges(self.surface)
            
        screen.blit( self.surface, self.s_pos )
        
    def send_message(self):
        self.messages.append({ "user": "user", "text": self.text_bar_msg["text"]})
        self.text_bar_msg["text"] = self.text_bar_placeholder
        
    def fade_in_anim(self, screen, w):
        self.scene_manager.loop_of("Map View", screen)
        self.s_pos -= pygame.Vector2( w / self.show_time, 0)
        
    def fade_out_anim(self, screen, w):
        self.scene_manager.loop_of("Map View", screen)
        self.s_pos += pygame.Vector2( w / self.show_time, 0)
        if self.frame_count >= self.fade_frame:
            self.scene_manager.go_to("Map View")
            self.fade_frame = -1
            self.frame_count = 0