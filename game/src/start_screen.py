import pygame
import time  # Import time module

from settings import TITLE
from credits import CreditsScreen  # Import the CreditsScreen class

class StartScreen:
    def __init__(self, screen, width, height):
        self.start = False
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font("game/src/assets/fonts/goblin.otf", 50)
        self.font2 = pygame.font.Font("game/src/assets/fonts/homevideo.ttf", 50)

        self.button_font = pygame.font.Font("game/src/assets/fonts/goblin.otf", 20)
        
        self.image = pygame.image.load('game/src/assets/game_over/lightcafe.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))  # Redimensionar a imagem para caber na tela
        
        
        self.title_text = self.font.render(TITLE, True, (255, 255, 255))
        self.button_text = self.font2.render("▶️ Iniciar", True, (255, 255, 255))
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
        self.blink_font = pygame.font.Font("game/src/assets/fonts/homevideo.ttf", 30)
        self.blink_text = self.blink_font.render("Pressione enter para pular", True, (255, 255, 255))
        self.blink_rect = self.blink_text.get_rect(center=(self.width // 2, self.height - 50))
        
    def show_info(self):
        info_font = pygame.font.Font("game/src/assets/fonts/homevideo.ttf", 23)
        lines1 = [
            "Bem vindo ao Light Café!",
            "A escuridão avança e a sua única defesa é um cafezinho.",
            "Não desperdice nenhum ingrediente,",
            "ou seu destino será trevoso"
        ]
        lines2 = [
            "Use as teclas laterais para se mover",
            "e dar sabor ao seu café!",
            "◀️     ▶️",
            "Boa sorte!"
        ]
        self.screen.fill((6, 2, 37))
        y_offset = 100
        line_spacing = 30  # Add spacing between lines
        for line in lines1:
            info_text = info_font.render(line, True, (255, 255, 255))
            self.screen.blit(info_text, (self.width // 2 - info_text.get_width() // 2, y_offset))
            y_offset += info_font.get_height() + line_spacing 

        y_offset += 150
        for line in lines2:
            info_text = info_font.render(line, True, (255, 255, 255))
            self.screen.blit(info_text, (self.width // 2 - info_text.get_width() // 2 , y_offset))
            y_offset += info_font.get_height() + line_spacing

        pygame.display.flip()
        start_time = time.time()
        while time.time() - start_time < 8:  # Wait for 8 seconds
            self.screen.fill((6, 2, 37))
            y_offset = 100
            for line in lines1:
                info_text = info_font.render(line, True, (255, 255, 255))
                self.screen.blit(info_text, (self.width // 2 - info_text.get_width() // 2, y_offset))
                y_offset += info_font.get_height() + line_spacing 

            y_offset += 150
            for line in lines2:
                info_text = info_font.render(line, True, (255, 255, 255))
                self.screen.blit(info_text, (self.width // 2 - info_text.get_width() // 2 , y_offset))
                y_offset += info_font.get_height() + line_spacing

            # Blinking text
            if int(time.time() * 2) % 2 == 0:  # Toggle every half second
                self.screen.blit(self.blink_text, self.blink_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.start = False
                    return

    def show(self):
        self.screen.fill((6, 2, 37))
        
        self.screen.blit(self.image, (self.width // 2 - self.image.get_width() // 2, 50))  # Desenhar a imagem de game over

        # self.screen.blit(self.title_text, (self.width // 2 - self.title_text.get_width() // 2, self.height // 2 - 100))
        
        pygame.draw.rect(self.screen, (0, 51, 102), self.button_rect)
        button_text_x = self.button_rect.x + (self.button_rect.width - self.button_text.get_width()) // 2
        button_text_y = self.button_rect.y + (self.button_rect.height - self.button_text.get_height()) // 2
        self.screen.blit(self.button_text, (button_text_x, button_text_y))
        
        pygame.draw.rect(self.screen, (6, 2, 37), self.button_credits_rect)
        button_credits_x = self.button_credits_rect.x + (self.button_credits_rect.width - self.button_credits.get_width()) // 2
        button_credits_y = self.button_credits_rect.y + (self.button_credits_rect.height - self.button_credits.get_height()) // 2
        
        self.screen.blit(self.button_credits, (button_credits_x, button_credits_y))
        
        pygame.display.flip()

        self.start = True
        while self.start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start = False
                    return False 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        self.start = False
                        self.show_info()
                        return True 
                    elif self.button_credits_rect.collidepoint(event.pos):
                        credits_screen = CreditsScreen(self.screen, self.width, self.height)
                        credits_screen.run()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: 
                        self.start = False
                        self.show_info()
                        return True