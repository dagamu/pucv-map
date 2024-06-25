import pygame
import argparse
from pyvidplayer2 import Video

from assets import AssetManager
from scenes.scene_manager import SceneManager
from animator.animator import Animator

WIDTH = 1440
HEIGHT = 900

bg_video = Video("white_bg.mp4")
bg_video.seek(15)

class App:
    def __init__(self, WIDTH, HEIGHT):
        self.window_size = (WIDTH, HEIGHT)
        self.FPS = 60
        
        parser = argparse.ArgumentParser(description='PUCV Map prototype')
        parser.add_argument( 'scene_number', type=int, nargs='?', default=0 )
        args = parser.parse_args()
        
        self.running = False
        self.asset_manager = AssetManager()
        self.animator = Animator()
        self.scene_manager = SceneManager( self.animator, self.asset_manager, args.scene_number)
        
        self.frame_count = 0
        self.state = 0 # 0: Nombres, 1: Nada, 2: App, 3: Nada, 4: Final
        self.opacity = 0
        self.op_vel = 8
        
    
    def run(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN ) #
        pygame.display.set_caption('Mapa PUCV')
        
        self.app_surf = pygame.Surface((360,698))
        self.vid_surf = pygame.Surface( bg_video.original_size )
        
        self.asset_manager.load()
        self.scene_manager.set_scenes()
        
        self.mask = self.asset_manager.get("mask")
        
        self.running = True
        while self.running:
            self.loop()
        pygame.quit()
        
    def loop(self):
        self.event_check()
        self.frame_count += 1
        self.screen.fill("white")
        bg_video.draw( self.vid_surf, (0,0), force_draw=True, )
        resize = pygame.transform.smoothscale( self.vid_surf, (WIDTH, HEIGHT) )
        self.screen.blit( resize, (0,0) )
        
        self.animator.loop()
        
        if self.state == 0:
            img = self.asset_manager.get("pre1").convert_alpha()
            img.fill((255, 255, 255, self.opacity), special_flags=pygame.BLEND_RGBA_MULT)
            self.screen.blit( img, (30,40) )
            
            if self.op_vel < 0:
                self.op_vel *= -1
                
        elif self.state == 1 or self.state == 3:
            if self.op_vel > 0:
                self.op_vel *= -1
                
        elif self.state == 2:
            
            self.scene_manager.current_scene.loop( self.app_surf )

            mask_surf = self.mask.copy()
            mask_surf.blit(self.app_surf, (0, 0), None, pygame.BLEND_RGBA_MULT )
            mockup_img = self.asset_manager.get("mockup").convert_alpha()
            
            mockup_img.fill((255, 255, 255, self.opacity), special_flags=pygame.BLEND_RGBA_MULT)
            mask_surf.fill((255, 255, 255, self.opacity), special_flags=pygame.BLEND_RGBA_MULT)
            
            self.screen.blit( mockup_img, (540, 70))
            self.screen.blit( mask_surf, (540, 70))
            
            if self.op_vel < 0:
                self.op_vel *= -1
        
        elif self.state == 4:
            img = self.asset_manager.get("pre2").convert_alpha()
            img.fill((255, 255, 255, self.opacity), special_flags=pygame.BLEND_RGBA_MULT)
            
            self.screen.blit( img, (30,40) )
            
            if self.op_vel < 0:
                self.op_vel *= -1
                
        self.opacity = pygame.math.clamp( self.opacity + self.op_vel, 0, 255 )
        
        if self.frame_count > 650:
            self.frame_count = 0
            bg_video.restart()
            bg_video.seek(15)
        
        pygame.display.flip()
        self.clock.tick( self.FPS )
        
    def event_check(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
                bg_video.close()
            elif e.type == pygame.MOUSEBUTTONUP:
                #print(self.opacity)
                pass
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_LCTRL:
                    self.state = (self.state + 1) % 5
                elif e.key == pygame.K_LSHIFT:
                    self.state = (self.state - 1) % 5
            self.scene_manager.current_scene.event_handler.handle_event(e, mouse_offset=pygame.Vector2(524, 47))
            

def main():
    app = App(WIDTH, HEIGHT)
    app.run()
    
if __name__ == "__main__":
    main()
