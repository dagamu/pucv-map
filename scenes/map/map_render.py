import pygame

class MapRender:
    def __init__( self, map):
        self.map = map
        
    def get_box_center( self, points ):
        x = [ p[0] for p in points ]
        y = [ p[1] for p in points ]
        return (sum(x) / len(points), sum(y) / len(points))
    
    def render_box_label( self, box, font ):
        return font.render( box["name"], True, "white")
    
    def draw( self ):
        font = self.map.asset_manager.font
        box_selected = False
        map_render = pygame.Surface( self.map.original_size )
        map_render.fill( self.map.opt["background-color"] )
        
        pygame.draw.polygon( map_render, (26, 38, 54), self.map.background )
        
        for box in self.map.boxes:
            if box == box_selected:
                pygame.draw.polygon( map_render, "green", box["points"], width=2 ) 
            pygame.draw.polygon( map_render, (38, 52, 78), box["points"] ) 
            box_center = self.get_box_center( box["points"])
            box["box_center"] = box_center
            
            box_label = self.render_box_label( box, font )
            
            w, h = box_label.get_size()
            offset = (0,0)
            if "label-offset" in box.keys():
                offset = box["label-offset"]
            label_pos = ( box_center[0] + offset[0] - w/2, box_center[1] + offset[1] - h/2 )
            map_render.blit( box_label, label_pos )
        
        for points in self.map.green_areas:
            pygame.draw.polygon( map_render, (20, 64, 67), points )
        
        for line in self.map.lines:
            pygame.draw.polygon( map_render, (68, 86, 110), line["points"] ) 
                   
        for i in self.map.icons:
            if "render" in i.keys():
                map_render.blit( i["render"], i["pos"] )
            
        for i in range(len(self.map.path)-2):
            point = self.map.path[i]
            start_p = point
            end_p = self.map.path[i+1]
            pygame.draw.line( map_render,  (0,0,255,100), start_p, end_p, width=5 )
            
        return map_render