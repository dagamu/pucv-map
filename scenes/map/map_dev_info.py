import pygame

class MapDevInfo:
    def __init__(self, scene):
        self.scene = scene
        self.start_pos = pygame.Vector2(50,100)
        self.info_values = {
            "map_pos": { "get_value": self.scene.map.get_pos },
            "zoom": { "get_value": self.scene.map.get_zoom },
            "box_selected": { "get_value": self.scene.get_box_selected }
        }
        
    def load(self):
        self.font = self.scene.asset_manager.font
        
    def render( self, screen ):
        for i, (name, value) in enumerate( self.info_values.items() ):
            current_value = value["get_value"]()
            render_doesnt_exists = not "render" in value.keys()
            if render_doesnt_exists or str(current_value) != value["text"]:
                self.render_line( current_value, name, value )
            screen.blit( value["render"], self.start_pos + pygame.Vector2(0, i*15) )
            
    def render_line( self, current_value, name, value ):
        text_to_render = str(f"{name}: {current_value}")
        value["render"] = self.font.render( text_to_render, True, "white" )
        value["text"] = str(current_value)[:]
        
    