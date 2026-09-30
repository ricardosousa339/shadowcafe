import pygame
from utils import get_asset_path

class FallingObject:
    _cached_skins = {}

    def __init__(self, width: int, height: int, x: float, y: float, speed: float, skin: int):
        self.speed = speed
        self.x = float(x)
        self.y = float(y)
        
        cache_key = (width, height)
        if cache_key not in FallingObject._cached_skins:
            raw_skins = {
                "torrao": get_asset_path("torraodeacucar.png"),
                "grao": get_asset_path("graodecafe.png")
            }
            FallingObject._cached_skins[cache_key] = {
                name: pygame.transform.scale(pygame.image.load(path).convert_alpha(), (width, height))
                for name, path in raw_skins.items()
            }
            
        self.skins = FallingObject._cached_skins[cache_key]
        self.current_skin = list(self.skins.keys())[skin]
        self.rect = self.skins[self.current_skin].get_rect(topleft=(int(x), int(y)))

    def set_skin(self, name):
        if name in self.skins:
            self.current_skin = name

    def update(self):
        self.y += self.speed
        self.rect.y = int(self.y)

    def draw(self, screen):
        screen.blit(self.skins[self.current_skin], self.rect)
