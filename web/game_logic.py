import asyncio
import random
import pygame

from falling_object import FallingObject
from game_over import GameOverScreen
from start_screen import StartScreen
from settings import INITIAL_SPEED, WIDTH, HEIGHT, TITLE
from player import Player
from background import Background
from utils import get_asset_path

class Game:
    def __init__(self):
        pygame.init()
        try:
            pygame.mixer.init()
        except Exception as e:
            print("Mixer init warning:", e)
            
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
        try:
            self.collision_sound = pygame.mixer.Sound(get_asset_path('drop.ogg'))
        except Exception as e:
            print("Sound load warning:", e)
            self.collision_sound = None

        self.reset()

    def reset(self):
        """Reinicia o estado da partida sem recriar a janela do Pygame."""
        self.running = True
        self.player = Player(300, 550, 0) 
        self.background = Background(WIDTH, HEIGHT)
        self.qtd_cafe = 0
        self.qtd_acucar = 0
        self.strikes = 0
        self.strike_flags = [False, False, False, False]
        
        self.flash_timer = 0
        self.flash_duration = 10
        self.falling_objects = []
        
        # Um novo item só surge depois que o anterior sumir da tela
        self.spawn_delay = 20  # ~0.3s de intervalo antes do próximo aparecer
        self.spawn_timer = 20  # Já começa pronto para soltar o primeiro item
        self.speed = 2.0       # Velocidade inicial fluida, que aumentará a cada item gerado

    async def run(self):
        start_screen = StartScreen(self.screen, WIDTH, HEIGHT)
        if not await start_screen.show():
            return

        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)
            await asyncio.sleep(0)
            
        game_over_screen = GameOverScreen(self.screen, WIDTH, HEIGHT, self.qtd_acucar, self.qtd_cafe)
        if await game_over_screen.show():
            self.reset()
            await self.run()

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
        
        # Um novo item SÓ aparece depois que o anterior sumir completamente da tela
        if len(self.falling_objects) == 0:
            self.spawn_timer += 1
            if self.spawn_timer >= self.spawn_delay:
                self.spawn_timer = 0
                x = random.randint(100, WIDTH - 100)
                
                # Aumenta a velocidade progressivamente a cada novo item
                self.speed += 0.12
                
                object_skin = random.randint(0, 1)
                fo_width = 40 if object_skin == 0 else 30
                fo_height = 40
                self.falling_objects.append(FallingObject(fo_width, fo_height, x, 0, self.speed, object_skin))

        for obj in list(self.falling_objects):
            obj.update()
            if obj.rect.colliderect(self.player.rect):
                if self.collision_sound:
                    try:
                        self.collision_sound.play()
                    except Exception:
                        pass

                if obj in self.falling_objects:
                    self.falling_objects.remove(obj)
                    
                if obj.current_skin == "grao":
                    self.qtd_cafe += 1
                    self.player.escurecer()
                elif obj.current_skin == "torrao":
                    self.qtd_acucar += 1
                    self.player.clarear()
            
            elif obj.rect.y >= HEIGHT - 200:
                if obj in self.falling_objects:
                    self.falling_objects.remove(obj)
                self.strikes += 1
                self.flash_timer = self.flash_duration
                self.player.marrom()

                if self.strikes == 1 and not self.strike_flags[0]:
                    self.background.set_background("cafeteria_3")
                    self.strike_flags[0] = True
                elif self.strikes == 2 and not self.strike_flags[1]:
                    self.background.set_background("cafeteria_2")
                    self.strike_flags[1] = True
                elif self.strikes == 3 and not self.strike_flags[2]:
                    self.background.set_background("cafeteria_1")
                    self.strike_flags[2] = True
                elif self.strikes >= 4 and not self.strike_flags[3]:
                    self.background.set_background("cafeteria_0")
                    self.strike_flags[3] = True
                    self.running = False

    def draw(self):
        self.background.draw(self.screen)
        self.player.draw(self.screen)
        for obj in self.falling_objects:
            obj.draw(self.screen)
                    
        escurecimento = (min(self.strikes, 4) / 4) * 0.8 * 255

        darken_surface = pygame.Surface((WIDTH, HEIGHT))
        darken_surface.set_alpha(int(escurecimento))
        darken_surface.fill((0, 0, 0))
        self.screen.blit(darken_surface, (0, 0))
        
        if self.flash_timer > 0:
            self.flash_timer -= 1
            flash_surface = pygame.Surface((WIDTH, HEIGHT))
            alpha = 80 if self.flash_timer % 10 < 5 else 20
            flash_surface.set_alpha(alpha)
            flash_surface.fill((255, 255, 255))
            self.screen.blit(flash_surface, (0, 0))
            
        pygame.display.flip()
