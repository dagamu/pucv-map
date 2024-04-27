import pygame

class MsgRender:
    def __init__(self, chat):
        self.chat = chat

    def text_render(self, text):
        font = self.chat.font
        render = font.render( text, True, "white")
        max_width = 145
        
        if render.get_size()[0] > max_width:
            words = text.split(" ")
            words_in_line = 1
            i = 0
            lines = []
            while i < len(words):
                while i + words_in_line <= len(words):
                    words_in_line += 1
                    line_text = " ".join(words[ i : i + words_in_line ])
                    line_width = font.size( line_text)[0]
                    if line_width >= max_width:
                        words_in_line -= 1
                        line_text = " ".join(words[ i : i + words_in_line ])
                        break
                
                line_render = font.render( line_text, True, "white")                                                                        
                i += words_in_line
                words_in_line = 1
                lines.append(line_render)
            
            render = pygame.Surface( (max_width, len(lines)*15+1) )
            render.fill("gray15")
            for i, line in enumerate(lines):
                render.blit( line, (0, i*15) )
        return render
    
    def draw_msg(self, i, msg, surface, y_pos, align):
        if not "render" in msg.keys():
            msg["render"] = self.text_render( msg["text"] )
                
        font_surface = msg["render"] 
        text_w, text_h = font_surface.get_size()
        
        w, h = surface.get_size()
        
        msg_box_points = {
            "left": [
                ( 86,  y_pos - 7 ), ( 252, y_pos - 7),
                ( 252, y_pos + text_h ), ( 96,  y_pos + text_h ),
                ( 96,  y_pos + 3 )
            ],
            "right": [
                ( w - 50,  y_pos - 7 ), ( w - 216, y_pos - 7),
                ( w - 216, y_pos + text_h ), ( w - 60,  y_pos + text_h ),
                ( w - 60,  y_pos + 3 )
            ]
        }
        
        if align == "left":
            pygame.draw.circle( surface, (21, 141, 201), (70, y_pos + 5), 15)
            text_x = 105
        else:
            text_x = w - 62 - text_w
        pygame.draw.polygon( surface, "gray15", msg_box_points[align] )
        surface.blit(font_surface, ( text_x, y_pos - 3))
        
        return text_h + 30
    
    def render_mesagges(self, surface):
        
        msgs = self.chat.messages
        y_pos = 125
        for i, msg in enumerate(msgs):
            if msg["user"] == "bot":
                y_pos += self.draw_msg(i, msg, surface, y_pos, align="left")
            else:
                y_pos += self.draw_msg(i, msg, surface, y_pos, align="right")