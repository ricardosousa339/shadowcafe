import pygame

from settings import HEIGHT, WIDTH

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('game/assets/xicara.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (180, 130))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = float(x)
        self.y = float(y)

    def update(self):
        keys = pygame.key.get_pressed()
        move_speed = 0.7  # Ajuste a velocidade de movimento conforme necessário
        if keys[pygame.K_LEFT]:
            self.x -= move_speed
        if keys[pygame.K_RIGHT]:
            self.x += move_speed


        self.x = max(0, min(self.x, WIDTH - self.rect.width))
        self.y = max(0, min(self.y, HEIGHT - self.rect.height))

        self.rect.topleft = (int(self.x), int(self.y))