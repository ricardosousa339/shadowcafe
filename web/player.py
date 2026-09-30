import pygame
from settings import HEIGHT, WIDTH
from utils import get_asset_path

class Player:
    def __init__(self, x, y, skin):
        self.x = float(x)
        self.y = float(y)
        
        skins = {
            "xicara_marrom": get_asset_path("xicara_marrom.png"),
            "xicara_escura": get_asset_path("xicara_escura.png"),
            "xicara_clara": get_asset_path("xicara_clara.png"),
        }
        
        self.skins = {
            name: pygame.transform.scale(pygame.image.load(path).convert_alpha(), (180, 130))
            for name, path in skins.items()
        }
        self.current_skin = list(self.skins.keys())[skin] 
        self.rect = self.skins[self.current_skin].get_rect(topleft=(int(x), int(y)))

    def update(self):
        keys = pygame.key.get_pressed()
        move_speed = 3.5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= move_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += move_speed

        self.x = max(0, min(self.x, WIDTH - self.rect.width))
        self.y = max(0, min(self.y, HEIGHT - self.rect.height))

        self.rect.topleft = (int(self.x), int(self.y))

    def set_background(self, name):
        if name in self.skins:
            self.current_skin = name

    def escurecer(self):
        self.current_skin = "xicara_escura"
    
    def clarear(self):
        self.current_skin = "xicara_clara"
    
    def marrom(self):
        self.current_skin = "xicara_marrom"
        
    def draw(self, screen):
        screen.blit(self.skins[self.current_skin], (int(self.x), int(self.y)))
