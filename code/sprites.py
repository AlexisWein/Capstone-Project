import pygame
from settings import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy()

class Bushes(Generic):
    def __init__(self, pos, surf, groups, name):
        super().__init__(pos, surf, groups)

class Alert(Generic):
    def __init__(self, pos, surf, groups, name):
        super().__init__(pos, surf, groups)

class Trees(Generic):
    def __init__(self, pos, surf, groups, name):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy().inflate((-10, -self.rect.height * 0.75))
        
class Buildings(Generic):
    def __init__(self, pos, surf, groups, name):
        super().__init__(pos, surf, groups)

class Road(Generic):
    def __init__(self, pos, surf, groups, name):
        super().__init__(pos, surf, groups)
        
class Interaction(Generic):
    def __init__(self, pos, size, groups, name):
        surf = pygame.Surface(size)
        super().__init__(pos, surf, groups)
        self.name = name