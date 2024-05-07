import pygame
from assets import AssetManager
#from maps.main_map import MAIN_MAP as MAP
from maps.ING_AU_map import ING_AU_MAP as MAP

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
        self.bg_img = self.asset_manager.get("ING_AU_map")
        
        self.map = MAP
        self.map.setup()
        self.map.load(self.asset_manager, scale=False)
        self.map_render = self.map.render
        
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
        
        self.running = True
        while self.running:
            self.loop()
        pygame.quit()
        
    def draw_nodes(self):
        def get_node_pos(id):
            for node in self.map.nodes:
                if node["id"] == id:
                    return node["pos"]
                
        for node in self.map.nodes:
            pygame.draw.circle( self.screen, "blue", node["pos"], 5 )
            self.screen.blit( self.font.render(str(node["id"]), True, "white"), node["pos"])
            for line in node["link"]:
                pygame.draw.line( self.screen, (0,255,0,120), node["pos"], get_node_pos(line) )
        
    def loop(self):
        self.quit_check()
        self.screen.fill( (7, 8, 12) ) 
       
        #self.screen.blit( self.bg_img, (0,0) )
        self.screen.blit( self.map_render, (0,0) )
        
        #pygame.draw.rect( self.screen, "green", self.map.boundaries, width=3 )
        #self.draw_nodes()
        
        
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos != self.mouse_label["value"] or not "render" in self.mouse_label.keys():
            self.mouse_label["value"] = mouse_pos
            self.mouse_label["text"] = str(mouse_pos)
            self.mouse_label["render"] = self.font.render( str(mouse_pos), True, "white")
        
        #self.screen.blit( self.mouse_label["render"], (10, 10) )
        
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