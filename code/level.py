import pygame
from settings import *
from player import Player
from sprites import Generic, Bushes, Trees, Buildings, Interaction, Alert
from pytmx.util_pygame import load_pygame
from support import *

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        tmx_data = load_pygame('../data/map.tmx')
        
        # trees
        for obj in tmx_data.get_layer_by_name('Trees'):
            Trees((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites], obj.name)
            
        # Alert
        for obj in tmx_data.get_layer_by_name('Alert'):
            Alert((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites, self.interaction_sprites], obj.name)
            
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
                    collision_sprites=self.collision_sprites,
                    interaction = self.interaction_sprites)

        Generic(
            pos = (0,0),
            surf = pygame.image.load('../graphics/world/map.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['Grass'])
            
            
    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            xLoc = self.player.pos.x
            yLoc = self.player.pos.y
            #Queen’s
            if (xLoc <= 2352 and xLoc >= 2162) and (yLoc <= 1418 and yLoc >= 1338):
                self.display_surface.blit(pygame.Surface((1000,500)),(480,580))
                fontTitle = pygame.font.SysFont(None, 60)
                paragraph = pygame.font.SysFont(None, 36)
                
                title = fontTitle.render("Queen's Court", True, WHITE)
                text1 = paragraph.render("Queen’s Court is a combination of three halls - St. John's, Robert's, and Bishop's", True, WHITE)
                text2 = paragraph.render("Each is steeped in the history and traditions of Fordham University.", True, WHITE)
                text3 = paragraph.render("150 First Years committed to high standards of living", True, WHITE)
                text4 = paragraph.render("Room Types: Double and Converted Triples", True, WHITE)
                text5 = paragraph.render("Co-ed with wings being either all male or female", True, WHITE)
                text6 = paragraph.render("Community bathrooms for St. John’s and Robert’s Halls", True, WHITE)
                text7 = paragraph.render("Private bathrooms for Bishop's Hall", True, WHITE)
                text8 = paragraph.render("Once a Queen's Courter, always a Queen's Courter!", True, WHITE)
                self.display_surface.blit(title, (820,580))
                self.display_surface.blit(text1, (480, 660))
                self.display_surface.blit(text2, (480, 700))
                self.display_surface.blit(text3, (480, 740))
                self.display_surface.blit(text4, (480, 780))
                self.display_surface.blit(text5, (480, 820))
                self.display_surface.blit(text6, (480, 860))
                self.display_surface.blit(text7, (480, 900))
                self.display_surface.blit(text8, (480, 940))
                #Example of above but simplified
                #position = 660
                #text = ["Queen’s Court is a combination of three halls",
                #" — St. John’s Hall, Robert’s Hall, and Bishop’s Hall.",
                #"Each is steeped in the history and traditions of",
                #"Fordham University.",
                #"150 First Years committed to high standards of living",
                #"Room Types: Double and Converted Triples",
                #"Co-ed with wings being either all male or female",
                #"Community bathrooms for St. John’s and Robert’s Halls",
                #"Private bathrooms for Bishop's Hall"]
                #label = []
                #for line in text:
                #    label.append(paragraph.render(line, True, WHITE))
                #    position+=10
                #return label, position
                #for line in range(len(label)):
                #    self.display_surface.blit(label(line), (480,position))
            #Hughes
            if (xLoc <= 2695 and xLoc >= 2495) and (yLoc <= 3475 and yLoc >= 3325):
                self.display_surface.blit(pygame.Surface((1000,500)),(480,580))
                fontTitle = pygame.font.SysFont(None, 60)
                paragraph = pygame.font.SysFont(None, 36)
                
                title = fontTitle.render("Hughes Hall", True, WHITE)
                text1 = paragraph.render("Hughes Hall is where business lives at Rose Hill.", True, WHITE)
                text2 = paragraph.render("The Gabelli School of Business moved into this building in 2012", True, WHITE)
                text3 = paragraph.render("The building was renovated and only the 1890s exterior remains.", True, WHITE)
                text4 = paragraph.render("What lies inside is a state-of-the-art center for business education with:", True, WHITE)
                text5 = paragraph.render("An in-house trading room with 15 Bloomberg terminals.", True, WHITE)
                text6 = paragraph.render("Video conference rooms. Interview with an overseas company by Skype.", True, WHITE)
                text7 = paragraph.render("A student lounge with iMacs, giant flat-screen TVs, and tables.", True, WHITE)
                text8 = paragraph.render("This is the kind of building where tomorrow's business leaders get their start!", True, WHITE)
                self.display_surface.blit(title, (820,580))
                self.display_surface.blit(text1, (480, 660))
                self.display_surface.blit(text2, (480, 700))
                self.display_surface.blit(text3, (480, 740))
                self.display_surface.blit(text4, (480, 780))
                self.display_surface.blit(text5, (480, 820))
                self.display_surface.blit(text6, (480, 860))
                self.display_surface.blit(text7, (480, 900))
                self.display_surface.blit(text8, (480, 940))
            #Dealy
            if (xLoc <= 1400 and xLoc >= 1200) and (yLoc <= 3475 and yLoc >= 3325):
                self.display_surface.blit(pygame.Surface((1000,500)),(480,580))
                fontTitle = pygame.font.SysFont(None, 60)
                paragraph = pygame.font.SysFont(None, 36)
                
                title = fontTitle.render("Dealy Hall", True, WHITE)
                text1 = paragraph.render("Dealy Hall is currently the home to several class at Rose Hill.", True, WHITE)
                text2 = paragraph.render("Dealy Hall includes multiple seminar rooms as well.", True, WHITE)
                text3 = paragraph.render("The building houses several academic departments too, including:", True, WHITE)
                text4 = paragraph.render("The English Department", True, WHITE)
                text5 = paragraph.render("The Sociology Department", True, WHITE)
                text6 = paragraph.render("The Psychology Department", True, WHITE)
                text7 = paragraph.render("With these 3 departments, it's no wonder Dealy is a popular building on campus.", True, WHITE)
                text8 = paragraph.render("Make sure to learn Dealy's layout if you are in any of the 3 above departments!", True, WHITE)
                self.display_surface.blit(title, (820,580))
                self.display_surface.blit(text1, (480, 660))
                self.display_surface.blit(text2, (480, 700))
                self.display_surface.blit(text3, (480, 740))
                self.display_surface.blit(text4, (480, 780))
                self.display_surface.blit(text5, (480, 820))
                self.display_surface.blit(text6, (480, 860))
                self.display_surface.blit(text7, (480, 900))
                self.display_surface.blit(text8, (480, 940))
            #Eddies
            if (xLoc <= 2150 and xLoc >= 1950) and (yLoc <= 3745 and yLoc >= 3550):
                self.display_surface.blit(pygame.Surface((1000,500)),(480,580))
                fontTitle = pygame.font.SysFont(None, 60)
                paragraph = pygame.font.SysFont(None, 36)
                
                title = fontTitle.render("Eddie's Parade", True, WHITE)
                text1 = paragraph.render("Eddie's (Edward's) Parade  is available to students for casual use and recreation.", True, WHITE)
                text2 = paragraph.render("These activities include lounging, sun bathing, and small group sports.", True, WHITE)
                text3 = paragraph.render("Larger activities and sports are not allowed on Eddie's due to lawn maintenance.", True, WHITE)
                text4 = paragraph.render("Eddie's can be reserved for events by contacting Office of Student Involvement.", True, WHITE)
                text5 = paragraph.render("These events are often office, department, club, or organization events.", True, WHITE)
                text6 = paragraph.render("Named after Clarence R. Edwards, Eddie's Parade is a key part of Fordham Rose Hill.", True, WHITE)
                text7 = paragraph.render("A ground for recreation and relaxation alike, Eddie's is central to the campus.", True, WHITE)
                text8 = paragraph.render("Eddie's is also the site of the University's commencement ceremony each spring.", True, WHITE)
                self.display_surface.blit(title, (820,580))
                self.display_surface.blit(text1, (480, 660))
                self.display_surface.blit(text2, (480, 700))
                self.display_surface.blit(text3, (480, 740))
                self.display_surface.blit(text4, (480, 780))
                self.display_surface.blit(text5, (480, 820))
                self.display_surface.blit(text6, (480, 860))
                self.display_surface.blit(text7, (480, 900))
                self.display_surface.blit(text8, (480, 940))
            #Keating
            if (xLoc <= 2495 and xLoc >= 2305) and (yLoc <= 5755 and yLoc >= 5550):
                self.display_surface.blit(pygame.Surface((1000,500)),(480,580))
                fontTitle = pygame.font.SysFont(None, 60)
                paragraph = pygame.font.SysFont(None, 36)
                
                title = fontTitle.render("Keating Hall", True, WHITE)
                text1 = paragraph.render("Keating Hall is arguably the most prominent building on Rose Hill's campus.", True, WHITE)
                text2 = paragraph.render("The astounding gothic building overlooks Eddie's Parade, central to the campus.", True, WHITE)
                text3 = paragraph.render("As Rose Hill's 'centerpiece', it is home to the Graduate School of Arts and Sciences.", True, WHITE)
                text4 = paragraph.render("Keating is named after Joseph Keating, S.J. and began construction in the 1930s.", True, WHITE)
                text5 = paragraph.render("The beauty of the building has led to several films using Keating as a set piece.", True, WHITE)
                text6 = paragraph.render("Films include: Love Story (1970), The Exorcist (1973), and A Beautiful Mind (2001).", True, WHITE)
                text7 = paragraph.render("Keating was recently in a Verizon commercial with Paul Giamatti and Cecily Strong.", True, WHITE)
                text8 = paragraph.render("Keating, along with Eddie's, is the site of the University's commencement ceremony.", True, WHITE)
                self.display_surface.blit(title, (820,580))
                self.display_surface.blit(text1, (480, 660))
                self.display_surface.blit(text2, (480, 700))
                self.display_surface.blit(text3, (480, 740))
                self.display_surface.blit(text4, (480, 780))
                self.display_surface.blit(text5, (480, 820))
                self.display_surface.blit(text6, (480, 860))
                self.display_surface.blit(text7, (480, 900))
                self.display_surface.blit(text8, (480, 940))
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