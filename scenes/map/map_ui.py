import pygame

from scenes.map.map_dev_info import MapDevInfo

class MapUI:
    def __init__(self, scene):
        self.scene = scene
        self.show_dev_info = True
        self.dev_info = MapDevInfo( scene )
        
    def load(self):
        self.dev_info.load()
        
    def render( self, screen ):
        if self.show_dev_info:
            self.dev_info.render( screen )
         
    def toggle_dev_info(self):
        self.show_dev_info = not self.show_dev_info 
    