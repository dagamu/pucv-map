import pygame
from functools import reduce

class TextBox:
    
    def __init__( self, font ):
        self.font = font
        self.line_height = 15
        
    def get_text( self, text, max_width, p ):
        font = self.font
        lines = [ font.render( text, True, "white" ) ]
        
        w = self.line_width(lines[0])
        if w > max_width:
            lines = self.split_text_lines( text, max_width, p, font )
            
        return lines
            
    def split_text_lines( self, text, max_width, p, font ):
        words = text.split(" ")
        words_in_line = 1
        i = 0
        lines = []
        while i < len(words):
            while i + words_in_line <= len(words):
                words_in_line += 1
                line_text = " ".join(words[ i : i + words_in_line ])
                line_width = font.size(line_text)[0] + 2*p
                if line_width >= max_width:
                    words_in_line -= 1
                    line_text = " ".join(words[ i : i + words_in_line ])
                    break
            
            line_render = font.render( line_text, True, "white")                                                                        
            i += words_in_line
            words_in_line = 1
            lines.append(line_render)
        return lines
    
    def get_box( self, lines, max_width, p, bg_color, min_width, max_height ):
        get_max_width = lambda l1, l2: l1 if self.line_width(l1) > self.line_width(l2) else l2
        max_line_width = self.line_width( reduce( get_max_width, lines ) )
        
        w = max( min_width, min( max_width, max_line_width + 2*p ) )
        h = min( max_height, len(lines)*self.line_height + 2*p )
        
        box = pygame.Surface( (w, h), pygame.SRCALPHA   )
        box.fill(bg_color) 
        return box, w
            
    def line_width( self, line ):
        return line.get_size()[0]
    
    def render( self, text, align="left", p=0, max_box_width=100, bg_color="gray15", min_width=0, max_height=-1 ):
        
        line_height = self.line_height
        max_width = max_box_width - 2 * p
        max_height = float('inf') if max_height == -1 else max_height
        
        lines = self.get_text( text, max_width, p )
        render, w = self.get_box( lines, max_width, p, bg_color, min_width=min_width, max_height=max_height )
        
        for i, line in enumerate(lines):
            x_line = p if align == "left" else w - self.line_width(line) - p
            render.blit( line, ( x_line, i*line_height + p) )
    
        return render