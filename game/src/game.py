import random
import pygame
from falling_object import FallingObject
from game_over import GameOverScreen
from settings import INITIAL_SPEED, WIDTH, HEIGHT, TITLE
from player import Player
from background import Background

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(300, 550)  # Posição inicial do jogador
        self.background = Background(WIDTH, HEIGHT)
        self.qtd_cafe = 0
        self.qtd_acucar = 0
        self.strikes = 0
        self.strike_flags = [False, False, False, False]
        
        
        self.flash_timer = 0
        self.flash_duration = 10
        self.falling_objects = []
        self.spawn_timer = 0


    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            
        game_over_screen = GameOverScreen(self.screen, WIDTH, HEIGHT)
        if game_over_screen.show():
            self.__init__()  # Reiniciar o jogo
            self.run()

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
        object_skin = random.randint(0, 1)
        
        speed = INITIAL_SPEED
        
        
        if self.spawn_timer > 1000: 
            self.spawn_timer = 0
            x = random.randint(0, WIDTH - 50)
            speed += 0.05
            self.falling_objects.append(FallingObject(30,40,x, 0, speed, object_skin))

        for obj in self.falling_objects:
            obj.update()
            if obj.rect.colliderect(self.player.rect):
                self.falling_objects.remove(obj)
                if obj.current_skin == "grao":
                    self.qtd_cafe += 1
                elif obj.current_skin == "torrao":
                    self.qtd_acucar += 1
            
            if obj.rect.y >= HEIGHT  - 200:
                self.falling_objects.remove(obj)
                self.strikes += 1
                self.flash_timer = self.flash_duration

            if self.strikes == 1 and not self.strike_flags[0]:
                self.background.set_background("cafeteria_3")
                self.strike_flags[0] = True
            elif self.strikes == 2 and not self.strike_flags[1]:
                print("Warning: 2 strikes!")
                self.background.set_background("cafeteria_2")
                self.strike_flags[1] = True
            elif self.strikes == 3 and not self.strike_flags[2]:
                print("Warning: 3 strikes!")
                self.background.set_background("cafeteria_1")
                self.strike_flags[2] = True
            elif self.strikes == 4 and not self.strike_flags[3]:
                print("Game Over: 4 strikes!")
                self.background.set_background("cafeteria_0")
                self.strike_flags[3] = True
                self.running = False

        self.falling_objects = [obj for obj in self.falling_objects if obj.rect.y < HEIGHT - 200]


    def draw(self):
        self.background.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect) 
        for obj in self.falling_objects:
            obj.draw(self.screen)
                    # Aplicar camada semi-transparente para diminuir o brilho
                    
                    
        escurecimento = (self.strikes / 4) * 0.8 * 255

        darken_surface = pygame.Surface((WIDTH, HEIGHT))
        darken_surface.set_alpha(escurecimento)  # Ajuste o valor de alpha para controlar o nível de escurecimento
        darken_surface.fill((0, 0, 0))
        self.screen.blit(darken_surface, (0, 0))
        
        if self.flash_timer > 0:
            self.flash_timer -= 1
            flash_surface = pygame.Surface((WIDTH, HEIGHT))
            alpha = 80 if self.flash_timer % 10 < 5 else 20  # Alternar entre visível e invisível
            flash_surface.set_alpha(alpha)
            flash_surface.fill((255, 255, 255))
            self.screen.blit(flash_surface, (0, 0))
        pygame.display.flip()
    