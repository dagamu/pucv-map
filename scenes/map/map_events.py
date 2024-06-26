import pygame

from utils import scale_tuple, get_rect_polygon

class EventHandler:
    def __init__(self, scene):
        self.scene = scene
        self.dragging = False
        self.prev_mouse_pos = pygame.Vector2()
        
    def handle_event(self, e, mouse_offset=pygame.Vector2(0,0) ):
        self.scene.ui.event_manager.handle_event(e)
        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            self.handle_click(mouse_offset)
        elif e.type == pygame.MOUSEWHEEL:
            self.handle_wheel(e)
        elif e.type == pygame.KEYUP:
            self.handle_key_up(e)
            
    def handle_wheel(self, e):
        self.scene.map.change_zoom( e.y )
        self.scene.map.move( pygame.Vector2(e.x*-3,0) )
            
    def handle_key_up(self, e):
        if self.scene.ui.search_bar.focus:
            self.scene.ui.search_bar.handle_key( e )
        elif e.unicode == "i":
            self.scene.ui.dev_info.toggle()
        
    def handle_click(self, mouse_offset):
        pos = pygame.Vector2( pygame.mouse.get_pos() ) - mouse_offset
        
        def colllide_box( box, position ):
            if not "collider" in box.keys():
                box["collider"] = get_rect_polygon( box["points"] )
                
            rect = pygame.Rect( scale_tuple(box["collider"], self.scene.map.zoom) )
            return rect.collidepoint(position)
        
        if hasattr( self.scene, "building_info_render"):
            info_rect = self.scene.building_info_render.get_rect()
            info_rect = info_rect.move( self.scene.building_info_pos )
            if not info_rect.collidepoint(pos):
                if self.scene.box_selected == False:
                    self.scene.box_selected = False
                elif not colllide_box( self.scene.box_selected, pos - self.scene.map_pos ):
                    self.scene.box_selected = False
                
                
        for box in self.scene.map.boxes:
            if colllide_box(box, pos - self.scene.map.pos): # ***
                if self.scene.box_selected == box and "map-link" in box.keys():
                    self.scene.map = self.scene.maps_manager.get( box["map-link"] )
                    self.scene.set_viewport()
                    
                    self.scene.box_selected = False
                    return
                
                self.scene.box_selected = box
                self.scene.ui.building_infobox.pos = pygame.Vector2(0, 600)
                self.scene.ui.building_infobox.render()
        
        self.scene.ui.event_manager.handle_click( pos )
            
    def move_keys(self, keys ):
        x_change = int( keys[pygame.K_LEFT] ) - int( keys[pygame.K_RIGHT] )
        y_change = int( keys[pygame.K_UP  ] ) - int( keys[pygame.K_DOWN ] )
        pos_change = pygame.Vector2( x_change, y_change )
        self.scene.map.move( pos_change )
        
    def zoom_keys(self, keys):
        zoom_change = int( keys[pygame.K_z] ) - int( keys[pygame.K_x] )
        if zoom_change != 0:
            self.scene.map.change_zoom(zoom_change)
            
    def drag_check(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.Vector2( pygame.mouse.get_pos() )
            if self.dragging:
                self.scene.map.move(mouse_pos - self.prev_mouse_pos) 
            else:
                self.dragging = True
            self.prev_mouse_pos = mouse_pos
        else:
            self.dragging = False
            
    def check_loop(self):
        keys = pygame.key.get_pressed() 
        self.move_keys( keys )
        self.zoom_keys( keys )
        self.drag_check()