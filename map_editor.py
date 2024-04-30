import pygame
from assets import AssetManager

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
       
        # TOP-LEFT --> RIGHT 
        buildings = {
            "IBC":      [ (360, 385), (448, 385), (448, 428), (360, 430) ],
            "GEO":      [ (358, 360), (400, 360), (448, 373), (448, 382), (358, 382) ],
            "ING-AU":   [ (220, 520), (300, 520), (285, 580), (215, 580) ],
            "ICT":      [ (265, 360), (320, 360), (320, 438), (265, 440) ],
            "FIN":      [ (210, 370), (240, 370), (240, 440), (210, 440) ],
            "RA":       [ (150, 360), (207, 360), (207, 440), (150, 440) ]
        }
        
        streets = {
            "Errázuriz":    [ (  0, 220), ( 45, 225), (325, 300), (500, 350), 
                              (500, 385), (325, 335), ( 45, 270), (  0, 265) ],
            
            "A":            [ (  0, 340), (360, 345), (395, 355), (  0, 355)],
            "Brasil":       [ (  0, 443), (330, 443), (490, 430), (490, 450),
                              (345, 460), (  0, 460) ],
            
            "BrasilB":      [ (  0, 485), (345, 485), (490, 480), (490, 495), (345, 500), (0, 500) ]
        }
        
        land = [ (-20, 130), ( 95, 140), (160, 140), (230, 140), (275, 130), 
                 (340, 125), (425, 110), (640,  50), (640, 720), (-20, 720) ]
        
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos != self.mouse_label["value"] or not "render" in self.mouse_label.keys():
            self.mouse_label["value"] = mouse_pos
            self.mouse_label["text"] = str(mouse_pos)
            self.mouse_label["render"] = self.font.render( str(mouse_pos), True, "white")
            
        #self.screen.blit( self.bg_img, (0,0) )
        
        pygame.draw.polygon( self.screen, (26, 38, 54), land )
        
        for name, points in buildings.items():
            pygame.draw.polygon( self.screen, (38, 52, 78), points ) 
            
            # x = [p[0] for p in points]
            # y = [p[1] for p in points]
            # centroid = (sum(x) / len(points), sum(y) / len(points))
        
        for name, points in streets.items():
            pygame.draw.polygon( self.screen, (68, 86, 110), points ) 
        
        
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