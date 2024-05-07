import pygame

from map_ui.ui_events import UIEvents

from map_ui.components.map_dev_info import MapDevInfo
from map_ui.components.map_building_infobox import BuildingInfoBox
from map_ui.components.search_bar import SearchBar
from map_ui.components.return_btn import ReturnBtn

class MapUI:
    def __init__(self, scene):
        self.scene = scene
        
        self.event_manager = UIEvents( self, scene )
        
        self.building_infobox = BuildingInfoBox(scene)
        self.search_bar = SearchBar(scene)
        self.dev_info = MapDevInfo(scene)
        self.return_btn = ReturnBtn(scene)
        
        
    def load(self):
        self.dev_info.load()
        self.building_infobox.load()
        self.search_bar.load()
        self.return_btn.load()
        
        w, h = self.scene.window_size
        self.chat_btn_size = (80,80)
        self.chat_btn_pos = (w*.65, h*.8)
        self.chat_btn_rect = pygame.Rect( self.chat_btn_pos, self.chat_btn_size )
        
        pet_img = self.scene.asset_manager.get("pet")
        self.chat_btn_pet = pygame.transform.scale( pet_img, self.chat_btn_size )
        
    def render( self, screen ):
        if self.dev_info.show:
            self.dev_info.render( screen )
    
        screen.blit(self.chat_btn_pet, self.chat_btn_pos )
        
        self.return_btn.render( screen )
        self.search_bar.loop(screen)
         
     
    
    