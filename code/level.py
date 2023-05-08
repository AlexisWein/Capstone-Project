import pygame
from settings import *
from player import Player
from sprites import Generic, Bushes, Trees, Buildings, Interaction
from pytmx.util_pygame import load_pygame
from support import *

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        tmx_data = load_pygame('../data/map.tmx')
        
        # trees
        for obj in tmx_data.get_layer_by_name('Trees'):
            Trees((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites], obj.name)
        # Bushes
        for obj in tmx_data.get_layer_by_name('Bushes'):
            Bushes((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites], obj.name)
        # Buildings
        for obj in tmx_data.get_layer_by_name('Buildings'):
            Buildings((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites], obj.name)
            
        #Collision
        for x, y, surf in tmx_data.get_layer_by_name('Collision').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites)

        #Player
        #self.player = Player((960,960), self.all_sprites)
        for obj in tmx_data.get_layer_by_name('Player'):
            if obj.name == 'Start':
                self.player = Player(
                    pos=(obj.x, obj.y),
                    group=self.all_sprites,
                    collision_sprites=self.collision_sprites)

        Generic(
            pos = (0,0),
            surf = pygame.image.load('../graphics/world/RH.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['Grass'])
            
    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)