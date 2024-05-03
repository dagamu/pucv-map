import pygame

class Map:
    def __init__( self, size, background, boxes, lines, green_areas, icons, opt={} ):
        
        self.size = size
        self.background = background
        self.boxes = boxes
        self.lines = lines
        self.green_areas = green_areas
        self.icons = icons
        
        self.opt = {
            "background-color": (7, 8, 12),
            **opt
        }        
        
    def load(self, asset_manager):
        self.asset_manager = asset_manager
        for i in self.icons:
            i["render"] = self.asset_manager.get_icon( i["name"], (24, 24) )
    
    def get_box_center( self, points ):
        x = [ p[0] for p in points ]
        y = [ p[1] for p in points ]
        return (sum(x) / len(points), sum(y) / len(points))
    
    def render_box_label( self, box, zoom, font ):
        box_label = font.render( box["name"], True, "white")
            
        return box_label
    
    def render( self, font, zoom, box_selected ):
        map_render = pygame.Surface( self.size )
        map_render.fill( self.opt["background-color"] )
        
        pygame.draw.polygon( map_render, (26, 38, 54), self.background )
        
        for box in self.boxes:
            
            if box == box_selected:
                pygame.draw.polygon( map_render, "green", box["points"], width=2 ) 
            pygame.draw.polygon( map_render, (38, 52, 78), box["points"] ) 
            box_center = self.get_box_center( box["points"])
            
            box_label = self.render_box_label( box, zoom, font )
            
            w, h = box_label.get_size()
            map_render.blit( box_label, (box_center[0]-w/2, box_center[1]-h/2) )
        
        for points in self.green_areas:
            pygame.draw.polygon( map_render, (20, 64, 67), points )
        
        for line in self.lines:
            pygame.draw.polygon( map_render, (68, 86, 110), line["points"] ) 
            
            
        for i in self.icons:
            if "render" in i.keys():
                map_render.blit( i["render"], i["pos"] )
            
        return map_render