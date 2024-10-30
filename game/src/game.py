import random
import pygame
from falling_object import FallingObject
from settings import WIDTH, HEIGHT, TITLE
from player import Player
from background import Background

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(300, 500)  # Posição inicial do jogador
        self.background = Background(WIDTH, HEIGHT)
        
        self.falling_objects = []
        self.spawn_timer = 0


    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.background.set_background("cafeteria_0")
                elif event.key == pygame.K_2:
                    self.background.set_background("cafeteria_4")

    def update(self):
        self.player.update()
        self.spawn_timer += 1
        if self.spawn_timer > 1000: 
            self.spawn_timer = 0
            x = random.randint(0, WIDTH - 50)
            speed = random.uniform(0.4, 0.5)
            self.falling_objects.append(FallingObject(x, 0, speed))

        for obj in self.falling_objects:
            obj.update()
            if obj.rect.colliderect(self.player.rect):
                self.falling_objects.remove(obj)
                # Adicione lógica para quando o jogador pegar o objeto

        self.falling_objects = [obj for obj in self.falling_objects if obj.rect.y < HEIGHT]


    def draw(self):
        self.background.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect) 
        for obj in self.falling_objects:
            obj.draw(self.screen)
        pygame.display.flip()