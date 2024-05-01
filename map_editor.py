import pygame
from assets import AssetManager
from maps.main_map import MAIN_MAP

WIDTH = 1280 / 2
HEIGHT = 720 

class MapEditor:
    def __init__(self, WIDTH, HEIGHT):
        self.window_size = (WIDTH, HEIGHT)
        self.FPS = 60
        self.running = False
        
        self.mouse_label = { "text": "(0, 0)", "value": (0,0) }
        
    def preload(self):
        self.asset_manager = AssetManager()
        self.asset_manager.load()
        
        self.font = pygame.font.SysFont("Arial", 12) 
        self.bg_img = self.asset_manager.get("proto_map")
        
        w, h = self.bg_img.get_size()
        scaled_size = (w * HEIGHT/h, HEIGHT)
        self.bg_img = pygame.transform.scale( self.bg_img, scaled_size )
    
    def run(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MAP EDITOR")
        
        self.preload()
        
        self.running = True
        while self.running:
            self.loop()
        pygame.quit()
        
    def loop(self):
        self.quit_check()
        self.screen.fill( (7, 8, 12) ) 
       
        land, buildings, streets, green_areas = (MAIN_MAP.background, MAIN_MAP.boxes, MAIN_MAP.lines, MAIN_MAP.green_areas )
            
        #self.screen.blit( self.bg_img, (0,0) )
        
        pygame.draw.polygon( self.screen, (26, 38, 54), land )
        
        for b in buildings:
            points = b["points"]
            pygame.draw.polygon( self.screen, (38, 52, 78), points ) 
            if "collider" in b.keys():
                pygame.draw.rect( self.screen, "red", b["collider"], width=3)
            
        for points in green_areas:
            pygame.draw.polygon( self.screen, (20, 64, 67), points ) 
        
        for s in streets:
            points = s["points"]
            pygame.draw.polygon( self.screen, (68, 86, 110), points ) 
        
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos != self.mouse_label["value"] or not "render" in self.mouse_label.keys():
            self.mouse_label["value"] = mouse_pos
            self.mouse_label["text"] = str(mouse_pos)
            self.mouse_label["render"] = self.font.render( str(mouse_pos), True, "white")
        
        self.screen.blit( self.mouse_label["render"], (10, 10) )
        
        pygame.display.flip()
        self.clock.tick( self.FPS )
        
    def quit_check(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False

def main():
    game = MapEditor(WIDTH, HEIGHT)
    game.run()
    
if __name__ == "__main__":
    main()