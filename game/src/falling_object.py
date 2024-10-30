import pygame

class FallingObject:
    def __init__(self, x: float, y: float, speed: float):
        self.image = pygame.image.load('game/assets/torraodeacucar.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.x = x
        self.y = y

    def update(self):
        self.y += self.speed
        self.rect.y = int(self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)