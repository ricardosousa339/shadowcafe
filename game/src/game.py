import pygame
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)


    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.x -= 5
        if keys[pygame.K_RIGHT]:
            self.player.x += 5
        if keys[pygame.K_UP]:
            self.player.y -= 5
        if keys[pygame.K_DOWN]:
            self.player.y += 5

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, (255, 0, 0), self.player)
        pygame.display.flip()