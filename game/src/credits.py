import pygame
from game.src.utils import get_asset_path

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Credits")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Credits text
credits = [
    "Time de Desenvolvimento",
    "",
    "Desenvolvedor principal: RICARDO MACHADO",
    "Designer gráfico: MATEUS MACHADO",
    "",
    "",
    "Recursos utilizados de:",
    "",
    "pixabay.com/users/soul_serenity_ambience-6817262/",
    "",
    "https://pt.pngtree.com/freepng/",
    "coffee-cup-in-pixel-art-style_15977196.html?sol=downref&id=bef",
    "",
    "Obrigado por Jogar!"
]


class CreditsScreen:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.font = pygame.font.Font(get_asset_path("goblin.otf"), 10)
        self.width = width
        self.height = height
        self.scroll_y = height
        self.clock = pygame.time.Clock()
        self.credits = credits
        

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect(center=(x, y))
        surface.blit(textobj, textrect)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.screen.fill(BLACK)

            self.scroll_y -= 1
            if self.scroll_y < -len(self.credits) * 40:
                self.scroll_y = self.height

            for i, line in enumerate(self.credits):
                self.draw_text(line, self.font, WHITE, self.screen, self.width // 2, self.scroll_y + i * 40)

            pygame.display.flip()
            self.clock.tick(60)

        from game.src.start_screen import StartScreen
        start_screen = StartScreen(self.screen, WIDTH, HEIGHT)
        start_screen.show()

        return