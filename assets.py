import pygame
import os

class AssetManager:
    def __init__(self) -> None:
        self.images_paths = {
            "mockup": "phone-mockup.png",
            "phone_bg": "phone-bg.png",
            "app_loading": "app-loading.png",
            "app_menu": "app-menu.png",
            "mask": "mask-white.png",
            "mask-black": "mask.png",
            "proto_map": "proto_map.jpeg"
        }
        self.images = {}
        self.dirname = os.path.dirname(__file__)
    
    def load(self):
        self.font = pygame.font.SysFont( "Arial", 12 )
        for name, path in self.images_paths.items():
            self.images[name] = self.load_image(path)
        
    def load_image(self, filename):
        fullpath = os.path.join(self.dirname, 'assets', filename)
        return pygame.image.load(fullpath)
    
    def get(self, name):
        if name in self.images.keys():
            return self.images[name]