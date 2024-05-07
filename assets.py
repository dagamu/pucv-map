import pygame
import os

class AssetManager:
    def __init__(self) -> None:
        
        self.buildings = [ "IBC", "FIN", "GEO", "ICT", "ING-AU", "RA", "EIB"]
        self.images_paths = {
            "mockup":       [ "phone-mockup.png" ] ,
            "phone_bg":     [ "phone-bg.png" ],
            "app_loading":  [ "app-loading.png" ],
            "app_menu":     [ "app-menu.png" ],
            "mask":         [ "mask-white.png" ],
            "mask-black":   [ "mask.png" ],
            "proto_map":    [ "proto_map.jpeg" ],
            "ING_AU_map":   [ "ING_AU_proto.png" ],
            "pet":          [ "pet", "normal_mascota.png"]
        }
        
        for b in self.buildings:
            self.images_paths[f"{b}-photo"] = [ "buildings", f"{b}.jpg"]
        
        self.icons_paths = {
            "arrow-left": "arrow-left.svg",
            "send": "send.svg",
            "subway": "subway.png",
            "coffee": "coffee.svg",
            "computer-lab": "computer-lab.svg",
            "library": "library.svg",
            "music": "music.svg",
            "search": "search.svg",
            "go_to": "go_to.svg"
        }
        
        self.images = {}
        self.icons = {}
        
        self.dirname = os.path.dirname(__file__)
        
    
    def load(self):
        
        self.font = pygame.font.SysFont( "Proxima Nova", 14 )
        self.big_font = pygame.font.SysFont( "Proxima Nova", 24 )
        
        for name, path in self.images_paths.items():
            self.images[name] = self.load_image(path)
            
        for icon, path in self.icons_paths.items():
            self.icons[icon] = self.load_icon(path)
        
    def load_image(self, filename):
        fullpath = os.path.join(self.dirname, 'assets', *filename)
        return pygame.image.load(fullpath)
    
    def load_icon(self, filename):
        fullpath = os.path.join(self.dirname, 'assets', 'icons', filename )
        return pygame.image.load(fullpath)
    
    def get(self, name):
        if name in self.images.keys():
            return self.images[name]
        
    def get_icon(self, name, size="auto"):
        if name in self.icons.keys():
            icon = self.icons[name]
            if not size == "auto":
                icon = pygame.transform.scale( icon, size )
            return icon