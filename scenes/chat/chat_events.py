import pygame

class EventHandler:
    def __init__(self, scene):
        self.scene = scene
        
    def handle_event(self, e):
        if e.type == pygame.MOUSEBUTTONUP:
            self.handle_click()
        if e.type == pygame.KEYDOWN:
            self.handle_key_down(e)
                    
    def handle_key_down(self, e):
        if self.scene.text_bar_focus:
            if e.key == pygame.K_BACKSPACE:
                self.scene.text_bar_msg["text"] = self.scene.text_bar_msg["text"][:-1]
            elif e.key == pygame.K_RETURN:
                self.scene.send_message()
            else:
                if self.scene.text_bar_msg["text"] == self.scene.text_bar_placeholder:
                    self.scene.text_bar_msg["text"] = ""
                self.scene.text_bar_msg["text"] += e.unicode
                
    def handle_click(self):
        pos = pygame.mouse.get_pos()
        w, h = self.scene.window_size
        
        if 50 <= pos[0] <= 90 and 50 <= pos[1] <= 90:
            self.scene.fade_frame = self.scene.frame_count + self.scene.show_time
            
        self.scene.text_bar_focus = (80 <= pos[0] <= w - 100) and (h - 110 <= pos[1] <= h - 60)