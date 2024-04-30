import pygame

class Map:
    def __init__( self, size, background, boxes, lines, zoom_treshold ):
        self.size = size
        self.background = background
        self.boxes = boxes
        self.lines = lines
        self.zoom_treshold = zoom_treshold
        
    
    def get_box_center( self, points ):
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        return (sum(x) / len(points), sum(y) / len(points))
    
    def render_box_label( self, box, zoom, font ):
        box_label = font.render( box["name"], True, "white")
            
        return box_label
    
    def render( self, font, zoom ):
        map_render = pygame.Surface( self.size )
        
        pygame.draw.polygon( map_render, (26, 38, 54), self.background )
        
        for box in self.boxes:
            pygame.draw.polygon( map_render, (38, 52, 78), box["points"] ) 
            box_center = self.get_box_center( box["points"])
            
            box_label = self.render_box_label( box, zoom, font )
            
            w, h = box_label.get_size()
            map_render.blit( box_label, (box_center[0]-w/2, box_center[1]-h/2) )
        
        for line in self.lines:
            pygame.draw.polygon( map_render, (68, 86, 110), line["points"] ) 
            
        return map_render
    
    