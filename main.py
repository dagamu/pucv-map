import pygame
import os
import argparse

from assets import AssetManager
from scenes.scene_manager import SceneManager
from animator.animator import Animator

WIDTH = 360
HEIGHT = 698

WINDOW_SIZE = (1176, 0)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % WINDOW_SIZE

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
    
    def run(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Mapa PUCV')
        
        self.asset_manager.load()
        self.scene_manager.set_scenes()
        
        self.running = True
        while self.running:
            self.loop()
        pygame.quit()
        
    def loop(self):
        self.event_check()
        self.screen.fill("white")
        
        self.animator.loop()
        self.scene_manager.current_scene.loop( self.screen )
        
        mockup_img = self.asset_manager.get("mockup")
        self.screen.blit(mockup_img, (0, 0))
        
        pygame.display.flip()
        self.clock.tick( self.FPS )
        
    def event_check(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            self.scene_manager.current_scene.event_handler.handle_event(e)
            

def main():
    app = App(WIDTH, HEIGHT)
    app.run()
    
if __name__ == "__main__":
    main()
