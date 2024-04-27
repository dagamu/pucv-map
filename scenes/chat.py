import pygame
import pygame.display
from scenes.messages_render import MsgRender

class ChatScene:
    def __init__(self, scene_manager):
        self.scene_name = "Chat"
        
        self.event_handler = EventHandler(self)
        self.msg_render = MsgRender(self)
        self.scene_manager = scene_manager
        
        self.show_time = 15
        
        self.frame_count = 0
        self.fade_frame = -1
        
        self.text_bar_focus = True
        self.text_bar_placeholder = "Escribe tu mensaje"
        self.text_bar_msg = { "text": self.text_bar_placeholder }
        
        self.messages = [{ "user": "bot", "text": "Hola! ¿En qué te puedo ayudar?" }]
        
    def setup(self, asset_manager):
        self.asset_manager = asset_manager
        
        self.window_size = pygame.display.get_surface().get_size()
        self.surface = pygame.Surface( self.window_size )
        self.s_pos = pygame.Vector2( self.window_size[0], 0)
        
        self.font = pygame.font.SysFont("Arial", 12)
        
    
    def loop(self, screen):
        self.frame_count += 1
        w, h = self.window_size
        
        if self.frame_count <= self.show_time:
            self.fade_in_anim( screen, w )
            
        elif self.fade_frame > 0:
            self.fade_out_anim( screen, w )
            
        self.surface.fill("gray10")
        
        pygame.draw.rect( self.surface, "gray15", (0, h - 120, w, 120  )) # BOTTOM BAR
        pygame.draw.rect( self.surface, "gray10", (w-90, h - 110, 45, 50  )) # SEND
        pygame.draw.rect( self.surface, "gray15", ( 50, 50, 40, 40  )) # EXIT
    
        text_box_color = "gray11" if self.text_bar_focus else "gray10"
        pygame.draw.rect( self.surface, text_box_color, (80, h - 110, w - 180, 50  )) # TEXT AREA
        
        if not "render" in self.text_bar_msg.keys() or self.text_bar_msg["text-redered"] != self.text_bar_msg["text"]:
            self.text_bar_msg["render"] = self.font.render( self.text_bar_msg["text"], True, "white")
            self.text_bar_msg["text-redered"] = str( self.text_bar_msg["text"] )
        self.surface.blit( self.text_bar_msg["render"], (90, h - 105) )
        
        self.msg_render.render_mesagges(self.surface)
            
        screen.blit( self.surface, self.s_pos )
        
    def send_message(self):
        self.messages.append({ "user": "user", "text": self.text_bar_msg["text"]})
        self.text_bar_msg["text"] = self.text_bar_placeholder
        
    def fade_in_anim(self, screen, w):
        self.scene_manager.loop_of("Map View", screen)
        self.s_pos -= pygame.Vector2( w / self.show_time, 0)
        
    def fade_out_anim(self, screen, w):
        self.scene_manager.loop_of("Map View", screen)
        self.s_pos += pygame.Vector2( w / self.show_time, 0)
        if self.frame_count >= self.fade_frame:
            self.scene_manager.go_to("Map View")
            self.fade_frame = -1
            self.frame_count = 0
        
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