import pygame

from scenes.map.map_dev_info import MapDevInfo
from scenes.map.map_building_infobox import BuildingInfoBox

from utils import sum_tuples, alpha_gradient, scale_tuple
from math import sqrt

class MapUI:
    def __init__(self, scene):
        self.scene = scene
        self.show_dev_info = False
        
        self.building_infobox = BuildingInfoBox( scene )
        self.return_btn_rect = pygame.Rect(50,50,40,40)
        
        
        self.chat_btn = [ ["white", (280, 620), 30 ],
                         [ (21, 141, 201), (280, 620), 28 ] ]
        
        r = self.chat_btn[0][2]
        shadow_size = ( r*3, r*3 )
        shadow = pygame.Surface( shadow_size )
        #shadow = alpha_gradient( shadow, lambda x,y: 250 - sqrt((x-shadow_size[0]/2)**2+(y-shadow_size[1]/2)**2) / (r*2) * 250)
        self.shadow_pos = sum_tuples( self.chat_btn[0][1], scale_tuple(shadow_size, -0.5))
        self.chat_btn_shadow = shadow
        
    def load(self):
        self.dev_info = MapDevInfo( self.scene )
        self.dev_info.load()
        self.building_infobox.load()
        
        pet_img = self.scene.asset_manager.get("pet")
        self.chat_btn_pet = pygame.transform.scale( pet_img, (50,50))
        
    def render( self, screen ):
        if self.show_dev_info:
            self.dev_info.render( screen )
        
        #screen.blit( self.chat_btn_shadow, self.shadow_pos )
        #pygame.draw.circle( screen, *self.chat_btn[0] )
        pygame.draw.circle( screen, *self.chat_btn[1] )
        screen.blit(self.chat_btn_pet, sum_tuples( self.chat_btn[0][1], (-25, -28)) )
            
        pygame.draw.rect( screen, (38, 42, 79), self.return_btn_rect, border_radius=3 )
        screen.blit( self.scene.asset_manager.get_icon("arrow-left"), (58, 58) )
         
    def toggle_dev_info(self):
        self.show_dev_info = not self.show_dev_info 
    
    def handle_click( self, mpos ):
        if self.return_btn_rect.collidepoint( mpos ):
            action = self.scene.map.opt["return-action"]
            if action[0] == "scene":
                self.scene.scene_manager.go_to( action[1] )
            elif action[0] == "map":
                self.scene.map = self.scene.maps_manager.get( action[1] )