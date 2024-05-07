import pygame

class UIEvents:
    def __init__(self, ui, scene):
        self.ui = ui
        self.scene = scene
        
    def handle_event(self, e):
        pass
        
    def check_loop():
        pass
    
    def handle_click( self, mpos ):
        if self.ui.return_btn.rect.collidepoint( mpos ):
            action = self.scene.map.opt["return-action"]
            if action[0] == "scene":
                self.scene.scene_manager.go_to( action[1] )
            elif action[0] == "map":
                self.scene.map = self.scene.maps_manager.get( action[1] )
                
        if self.ui.search_bar.rect.collidepoint( mpos ):
            self.ui.search_bar.toggle_focus()
        else:
            self.ui.search_bar.focus = False
            
        if self.ui.chat_btn_rect.collidepoint( mpos ):
            self.scene.scene_manager.next_scene()
