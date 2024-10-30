import pygame

class FallingObject:
    def __init__(self, width, height, x: float, y: float, speed: float, skin: int):


        self.speed = speed
        self.x = x
        self.y = y
        
                        # Dicionário de fundos
        skins = {
            "torrao": "game/assets/torraodeacucar.png",
            "grao": "game/assets/graodecafe.png"
        }
        
        self.skins = {name: pygame.transform.scale(pygame.image.load(path).convert_alpha(), (width, height)) for name, path in skins.items()}

        
        self.current_skin = list(self.skins.keys())[skin]  

        self.rect = self.skins[self.current_skin].get_rect(topleft=(x, y))

    def set_skin(self, name):
        if name in self.skins:
            self.current_skin = name

    def update(self):
        self.y += self.speed
        self.rect.y = int(self.y)

    def draw(self, screen):
        screen.blit(self.skins[self.current_skin], self.rect)