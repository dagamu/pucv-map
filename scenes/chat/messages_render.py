import pygame
from textbox import TextBox

from utils import sum_tuples, scale_tuple

class MsgRender:
    def __init__(self, chat):
        self.chat = chat
        self.textbox = TextBox( self.chat.font )
    
    def draw_msg(self, msg, surface, y_pos, align):
        padding = 6
        if not "render" in msg.keys():
            msg["render"] = self.textbox.render( msg["text"], align, padding, max_box_width = 165 )
                
        font_surface = msg["render"] 
        text_w, text_h = font_surface.get_size()
        
        w, h = surface.get_size()
        
        msg_box_points = {
            "left": [ ( 86,  y_pos - 7 ), ( 96, y_pos - 7), ( 96,  y_pos + 3 ) ],
            "right": [ ( w - 50,  y_pos - 7 ), ( w - 60, y_pos - 7), ( w - 60,  y_pos + 3 ) ]
        }
        
        if align == "left":
            circle_pos = (70, y_pos + 5)
            img_size = self.chat.pet_img.get_size()
            img_pos = sum_tuples( circle_pos, scale_tuple(img_size,-0.5))
            pygame.draw.circle( surface, (21, 141, 201), (70, y_pos + 5), 15)
            surface.blit( self.chat.pet_img, img_pos )
            text_x = 96
        else:
            text_x = w - text_w - 60 
            
        pygame.draw.polygon( surface, "gray15", msg_box_points[align] )
        surface.blit(font_surface, ( text_x, y_pos - 7 ))
        
        return text_h + 30
    
    def render_mesagges(self, surface):
        
        msgs = self.chat.messages
        y_pos = 125
        for i, msg in enumerate(msgs):
            if msg["user"] == "bot":
                y_pos += self.draw_msg( msg, surface, y_pos, align="left")
            else:
                y_pos += self.draw_msg( msg, surface, y_pos, align="right")