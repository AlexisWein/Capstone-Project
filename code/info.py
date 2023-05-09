import pygame
from settings import *

class Info:
    def __init__(self, player, toggle_info):
        self.player = player
        self.toggle_info = toggle_info
        self.display_surface = pygame.display.get_surface()
        #self.font = pygame.font.Font('Arial', 30)
        
    def update(self):
        self.display_surface.blit(pygame.Surface(100,100),(100,100))