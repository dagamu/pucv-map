import pygame

from utils import scale_tuple, get_rect_polygon

class EventHandler:
    def __init__(self, scene):
        self.scene = scene
        self.dragging = False
        self.prev_mouse_pos = pygame.Vector2()
        
    def handle_event(self, e):
        if e.type == pygame.MOUSEBUTTONUP:
            self.handle_click()
        elif e.type == pygame.MOUSEWHEEL:
            self.scene.zoom += e.y * 0.05
            self.scene.update_scale()
        elif e.type == pygame.KEYUP:
            self.handle_key_up(e)
            
    def handle_key_up(self, e):
        if e.unicode == "i":
            self.scene.ui.toggle_dev_info()
        
    def handle_click(self):
        pos = pygame.Vector2( pygame.mouse.get_pos() )
        chat_btn_pos = pygame.Vector2( self.scene.chat_btn[0][1] )
        
        def colllide_box( box, position ):
            if not "collider" in box.keys():
                box["collider"] = get_rect_polygon( box["points"] )
                
            rect = pygame.Rect( scale_tuple(box["collider"], self.scene.zoom) )
            return rect.collidepoint(position)
        
        if hasattr( self.scene, "building_info_render"):
            info_rect = self.scene.building_info_render.get_rect()
            info_rect = info_rect.move( self.scene.building_info_pos )
            if not info_rect.collidepoint(pos):
                if self.scene.box_selected == False:
                    self.scene.box_selected = False
                elif not colllide_box( self.scene.box_selected, pos - self.scene.map_pos ):
                    self.scene.box_selected = False
                
                
        for box in self.scene.current_map.boxes:
            if colllide_box(box, pos - self.scene.map_pos):
                if self.scene.box_selected == box and "map-link" in box.keys():
                    self.scene.current_map = self.scene.maps_manager.get( box["map-link"])
                    self.scene.current_map.load(self.scene.asset_manager)
                    self.scene.box_selected = False
                    self.scene.map_render = self.scene.current_map.render( self.scene.asset_manager.font, self.scene.zoom, self.scene.box_selected )
                    self.original_map_size = self.scene.map_render.get_size()
                    self.map_size = self.original_map_size
                    
                    return
                self.scene.box_selected = box
                self.scene.building_info_pos = pygame.Vector2(0, 600)
                self.scene.render_building_info()
        
        if pos.distance_to( chat_btn_pos ) < self.scene.chat_btn[0][2]:
            self.scene.scene_manager.next_scene()
            
    def move_keys(self, keys ):
        if keys[pygame.K_LEFT]: 
            self.scene.map_pos.x += self.scene.move_vel
            self.scene.target_point.x += self.scene.move_vel / -self.scene.zoom
            
        if keys[pygame.K_RIGHT]: 
            self.scene.map_pos.x -= self.scene.move_vel
            self.scene.target_point.x -= self.scene.move_vel / -self.scene.zoom
              
        if keys[pygame.K_UP]: 
            self.scene.map_pos.y += self.scene.move_vel
            self.scene.target_point.y += self.scene.move_vel / -self.scene.zoom
               
        if keys[pygame.K_DOWN]:
            self.scene.map_pos.y -= self.scene.move_vel 
            self.scene.target_point.y -= self.scene.move_vel / -self.scene.zoom
        
    def zoom_keys(self, keys):
        if keys[pygame.K_z]:
            self.scene.zoom += 0.01
            self.scene.update_scale()
            
        if keys[pygame.K_x]:
            self.scene.zoom -= 0.01
            self.scene.update_scale()
            
    def drag_check(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.Vector2( pygame.mouse.get_pos() )
            if self.dragging:
                self.scene.map_pos += mouse_pos - self.prev_mouse_pos
                self.scene.target_point += (mouse_pos - self.prev_mouse_pos) / -self.scene.zoom
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