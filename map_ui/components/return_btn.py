import pygame

class ReturnBtn:
    def __init__(self, scene):
        self.scene = scene
        self.bg_color = (38, 42, 79)
        self.rect = pygame.Rect(50,50,40,40)
        
    def load(self, ):
        self.icon = self.scene.asset_manager.get_icon("arrow-left")
    
    def render( self, surf ):
        pygame.draw.rect( surf, self.bg_color, self.rect, border_radius=3 )
        surf.blit( self.icon, (58, 58) )