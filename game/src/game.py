import os
import random
import pygame
from game.src.falling_object import FallingObject
from game.src.game_over import GameOverScreen
from game.src.start_screen import StartScreen
from game.src.settings import INITIAL_SPEED, WIDTH, HEIGHT, TITLE
from game.src.player import Player
from game.src.background import Background
from game.src.utils import get_asset_path



class Game:
    def __init__(self):
        os.environ['SDL_AUDIODRIVER'] = 'pulse'

        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(300, 550, 0) 
        self.background = Background(WIDTH, HEIGHT)
        self.qtd_cafe = 0
        self.qtd_acucar = 0
        self.strikes = 0
        self.strike_flags = [False, False, False, False]
        self.max_timer = 1000
        
        
        self.flash_timer = 0
        self.flash_duration = 10
        self.falling_objects = []
        self.spawn_timer = 0
        self.speed = INITIAL_SPEED

        self.collision_sound = pygame.mixer.Sound(get_asset_path('drop.ogg'))


    def run(self):
        
        start_screen = StartScreen(self.screen, WIDTH, HEIGHT)
        if not start_screen.show():
            return

        while self.running:
            self.events()
            self.update()
            self.draw()
            
        game_over_screen = GameOverScreen(self.screen, WIDTH, HEIGHT, self.qtd_acucar, self.qtd_cafe)
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
        
        
        fo_width = 0
        fo_height = 0
        
        if object_skin == 0:
            fo_width = 40
            fo_height = 40
        elif object_skin == 1:
            fo_width = 30
            fo_height = 40
        
        
        if self.spawn_timer > self.max_timer: 
            self.spawn_timer = 0
            if self.max_timer > 300:
                self.max_timer -= 10
            x = random.randint(100, WIDTH - 100)
            self.speed += 0.008
            print(self.speed)
            self.falling_objects.append(FallingObject(fo_width, fo_height, x, 0, self.speed, object_skin))

        for obj in self.falling_objects:
            obj.update()
            if obj.rect.colliderect(self.player.rect):
                self.collision_sound.play()

                self.falling_objects.remove(obj)
                if obj.current_skin == "grao":
                    self.qtd_cafe += 1
                    self.player.escurecer()
                elif obj.current_skin == "torrao":
                    self.qtd_acucar += 1
                    self.player.clarear()
            
            if obj.rect.y >= HEIGHT  - 200:
                self.falling_objects.remove(obj)
                self.strikes += 1
                self.flash_timer = self.flash_duration
                self.player.marrom()

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

        # self.falling_objects = [obj for obj in self.falling_objects if obj.rect.y < HEIGHT - 200]


    def draw(self):
        self.background.draw(self.screen)
        self.player.draw(self.screen)
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
    