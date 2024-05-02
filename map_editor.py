import pygame
from assets import AssetManager
from maps.main_map import MAIN_MAP

WIDTH = 1280 / 2
HEIGHT = 720 

background = [
    (45,60), (245, 45), (245, 60), (320,40), (505,25), (505,430), (320, 400),
    (320, 395), (260, 380), (250, 440), (20, 480)
]

boxes = [
    {
        "name": "LAB-DOC 1-7",
        "points": [(50, 65), (130,60), (130,130), (45, 130) ]
    },
    {
        "name": "LAB-DOC 1-6",
        "points": [(150,160), (240,160), (240,245), (150,245)]
    },
    {
        "name": "LAB-DOC-1-4",
        "points": [(150,250), (240,250), (240,330), (150,330)]
    },
    {
        "name": "LAB-DOC-1-5",
        "points": [( 43, 160 ) ,( 128, 160 ) ,( 130, 245 ) ,( 38, 245 )]
    },
    {
        "name": "LAB-DOC-1-3",
        "points": [(38, 250), (130, 250), (130, 330), (35, 330)]
    },
    {
        "name": "LAB-DOC-1-2",
        "points": [(32, 365), (140, 365), (140, 450), (25, 470)]
    },
    {
        "name": "LAB-DOC-1-1",
        "points": [(145, 365), (195, 365), (195, 410), (240, 410), (240, 433 ), (145, 448)]
    },
    {
        "name": "ING-AU-1-2",
        "points": [(370, 170), (460, 170), (460, 245), (370, 245)]
    },
    {
        "name": "ING-AU-1-1",
        "points": [(330, 250), (460, 250), (460, 332), (318, 332)]
    },
    {
        "name": "ING-AU-COFFEE",
        "points": [(322, 160), (368, 160), (368, 245), (305, 245)]
    },
    {
        "name": "ING-AU-CHAPEL",
        "points": [(345, 400), (360, 365), (375, 370), (380, 365), (405, 370), (410, 365), (435, 380), (500, 380), (500, 420)]
    }
]

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
        self.bg_img = self.asset_manager.get("ING_AU_map")
        
        w, h = self.bg_img.get_size()
        scaled_size = (w * HEIGHT*.7/h, HEIGHT*.7)
        self.bg_img = pygame.transform.scale( self.bg_img, scaled_size )
    
    def run(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MAP EDITOR")
        
        self.preload()
        self.saved_points = []
        
        for b in boxes:
            b["label-render"] = self.font.render( b["name"], True, "white" )
        
        self.running = True
        while self.running:
            self.loop()
        pygame.quit()
        
    def loop(self):
        self.quit_check()
        self.screen.fill( (7, 8, 12) ) 
       
        # land, buildings, streets, green_areas, icons = 
        
        #self.screen.blit( self.bg_img, (0,0) )
        pygame.draw.polygon( self.screen, (26, 38, 54), background )
        
        for b in boxes:
            points = b["points"]
            pygame.draw.polygon( self.screen, (38, 52, 78), points ) 
            if "label-render" in b.keys():
                self.screen.blit( b["label-render"], points[0] )
            else:
                b["label-render"] = self.font.render( b["name"], True, "white" )
            if "collider" in b.keys():
                pygame.draw.rect( self.screen, "red", b["collider"], width=3)
                
        """
        for points in green_areas:
            pygame.draw.polygon( self.screen, (20, 64, 67), points ) 
        
        for s in streets:
            points = s["points"]
            pygame.draw.polygon( self.screen, (68, 86, 110), points ) 
            
        for i in icons:
            pos = i["pos"]
            self.screen.blit( self.asset_manager.get_icon(i["name"], (24, 24)), pos )
        
        """
        
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
            if e.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                x = x // 5 * 5
                y = y // 5 * 5
                self.saved_points.append((x,y))
            if e.type == pygame.KEYUP:
                if e.unicode == "v":
                    print(str(self.saved_points))
                    self.saved_points = []
            if e.type == pygame.QUIT:
                self.running = False

def main():
    game = MapEditor(WIDTH, HEIGHT)
    game.run()
    
if __name__ == "__main__":
    main()