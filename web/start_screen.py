import asyncio
import time
import pygame

from settings import TITLE
from credits import CreditsScreen
from utils import get_asset_path

class StartScreen:
    def __init__(self, screen, width, height):
        self.start = False
        self.screen = screen
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        
        self.font = pygame.font.Font(get_asset_path("goblin.otf"), 50)
        self.font2 = pygame.font.Font(get_asset_path("homevideo.ttf"), 50)
        self.button_font = pygame.font.Font(get_asset_path("goblin.otf"), 20)
        
        self.image = pygame.image.load(get_asset_path("lightcafe.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))
        
        self.title_text = self.font.render(TITLE, True, (255, 255, 255))
        self.button_text = self.font2.render("▶ Iniciar", True, (255, 255, 255))
        self.button_padding = 20
        self.button_rect = pygame.Rect(
            self.width // 2 - self.button_text.get_width() // 2 - self.button_padding,
            self.height // 2 + 100,
            self.button_text.get_width() + 2 * self.button_padding,
            self.button_text.get_height() + 2 * self.button_padding
        )
        self.button_credits = self.button_font.render("Créditos", True, (255, 255, 255))
        self.button_credits_rect = pygame.Rect(
            self.width // 2 - self.button_credits.get_width() // 2 - self.button_padding,
            self.height // 2 + 200,
            self.button_credits.get_width() + 2 * self.button_padding,
            self.button_credits.get_height() + 2 * self.button_padding
        )
        self.blink_font = pygame.font.Font(get_asset_path("homevideo.ttf"), 30)
        self.blink_text = self.blink_font.render("Pressione enter para pular", True, (255, 255, 255))
        self.blink_rect = self.blink_text.get_rect(center=(self.width // 2, self.height - 50))
        
    async def show_info(self):
        info_font = pygame.font.Font(get_asset_path("homevideo.ttf"), 23)
        lines1 = [
            "Bem vindo ao Light Café!",
            "A escuridão avança e a sua única defesa é um cafezinho.",
            "Não desperdice nenhum ingrediente,",
            "ou seu destino será trevoso"
        ]
        lines2 = [
            "Use as teclas laterais para se mover",
            "e dar sabor ao seu café!",
            "◀     ▶",
            "Boa sorte!"
        ]
        
        start_time = time.time()
        line_spacing = 30
        
        while time.time() - start_time < 8:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                    if event.type == pygame.MOUSEBUTTONDOWN or event.key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_ESCAPE):
                        return

            self.screen.fill((6, 2, 37))
            y_offset = 100
            for line in lines1:
                info_text = info_font.render(line, True, (255, 255, 255))
                self.screen.blit(info_text, (self.width // 2 - info_text.get_width() // 2, y_offset))
                y_offset += info_font.get_height() + line_spacing 

            y_offset += 150
            for line in lines2:
                info_text = info_font.render(line, True, (255, 255, 255))
                self.screen.blit(info_text, (self.width // 2 - info_text.get_width() // 2, y_offset))
                y_offset += info_font.get_height() + line_spacing

            # Texto piscando
            if int(time.time() * 2) % 2 == 0:
                self.screen.blit(self.blink_text, self.blink_rect)
                
            pygame.display.flip()
            self.clock.tick(60)
            await asyncio.sleep(0)

    async def show(self):
        self.start = True
        while self.start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start = False
                    return False 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        self.start = False
                        await self.show_info()
                        return True 
                    elif self.button_credits_rect.collidepoint(event.pos):
                        credits_screen = CreditsScreen(self.screen, self.width, self.height)
                        await credits_screen.run()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: 
                        self.start = False
                        await self.show_info()
                        return True

            self.screen.fill((6, 2, 37))
            self.screen.blit(self.image, (self.width // 2 - self.image.get_width() // 2, 50))
            
            # Botão Iniciar
            pygame.draw.rect(self.screen, (0, 51, 102), self.button_rect, border_radius=8)
            button_text_x = self.button_rect.x + (self.button_rect.width - self.button_text.get_width()) // 2
            button_text_y = self.button_rect.y + (self.button_rect.height - self.button_text.get_height()) // 2
            self.screen.blit(self.button_text, (button_text_x, button_text_y))
            
            # Botão Créditos
            pygame.draw.rect(self.screen, (6, 2, 37), self.button_credits_rect)
            button_credits_x = self.button_credits_rect.x + (self.button_credits_rect.width - self.button_credits.get_width()) // 2
            button_credits_y = self.button_credits_rect.y + (self.button_credits_rect.height - self.button_credits.get_height()) // 2
            self.screen.blit(self.button_credits, (button_credits_x, button_credits_y))
            
            pygame.display.flip()
            self.clock.tick(60)
            await asyncio.sleep(0)

        return True
