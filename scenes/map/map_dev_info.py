import pygame

class MapDevInfo:
    def __init__(self, scene):
        self.scene = scene
        self.start_pos = pygame.Vector2(50,60)
        self.info_values = {
            "map_pos": { "value": pygame.Vector2() },
            "zoom": { "value": 1 },
            "box_selected": { "value": False },
            "building_info_pos": { "value": (0,0) }
        }
        
    def load(self):
        self.font = self.scene.asset_manager.font
        
    def render( self, screen ):
        for i, (name, value) in enumerate( self.info_values.items() ):
            current_value = self.get_current_value( name )
            render_exists = not "render" in value.keys()
            if render_exists or str(current_value) != value["text"]:
                self.render_line( current_value, name, value )
            screen.blit( value["render"], self.start_pos + pygame.Vector2(0, i*15) )
            
    def render_line( self, current_value, name, value ):
        text_to_render = str(f"{name}: {current_value}")
        value["render"] = self.font.render( text_to_render, True, "white" )
        value["text"] = str(current_value)
        value["value"] = current_value
        
        
    def get_current_value( self, name ):
        val = self.scene.__dict__[name]
        is_float = type(val) is float
        current_value = round( val, 3 ) if is_float else val
        return current_value