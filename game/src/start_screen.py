import pygame

from settings import TITLE

class StartScreen:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font("game/assets/fonts/goblin.otf", 50)
        self.font2 = pygame.font.Font("game/assets/fonts/homevideo.ttf", 50)

        self.button_font = pygame.font.Font("game/assets/fonts/goblin.otf", 20)
        
        self.image = pygame.image.load('game/assets/game_over/lightcafe.png').convert_alpha()
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
        
        
        
    def show(self):
        self.screen.fill((6, 2, 37))
        
        self.screen.blit(self.image, (self.width // 2 - self.image.get_width() // 2, 50))  # Desenhar a imagem de game over

        # self.screen.blit(self.title_text, (self.width // 2 - self.title_text.get_width() // 2, self.height // 2 - 100))
        
        pygame.draw.rect(self.screen, (0, 51, 102), self.button_rect)
        button_text_x = self.button_rect.x + (self.button_rect.width - self.button_text.get_width()) // 2
        button_text_y = self.button_rect.y + (self.button_rect.height - self.button_text.get_height()) // 2
        self.screen.blit(self.button_text, (button_text_x, button_text_y))
        
        button_credits_x = self.button_rect.x + (self.button_rect.width - self.button_credits.get_width()) // 2
        button_credits_y = self.button_rect.y + (self.button_rect.height - self.button_credits.get_height()) // 2 + 50
        
        self.screen.blit(self.button_credits, (button_credits_x, button_credits_y + 50))
        
        pygame.display.flip()

        # Loop para manter a tela de início até ser fechada
        start = True
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                    return False  # Indica que o jogo deve ser encerrado
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        start = False
                        return True  # Indica que o jogo deve ser iniciado
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Pressionar Enter para iniciar o jogo
                        start = False
                        return True  # Indica que o jogo deve ser iniciado