import asyncio
import pygame
from utils import get_asset_path

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CREDITS_TEXT = [
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
    "Obrigado por Jogar!",
    "",
    "(Pressione ESC, ENTER ou clique para voltar)"
]

class CreditsScreen:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(get_asset_path("goblin.otf"), 12)
        self.scroll_y = height
        self.clock = pygame.time.Clock()
        self.credits = CREDITS_TEXT

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect(center=(x, y))
        surface.blit(textobj, textrect)

    async def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return
                    if event.key in (pygame.K_ESCAPE, pygame.K_RETURN, pygame.K_SPACE):
                        return

            self.screen.fill(BLACK)

            self.scroll_y -= 1.5
            if self.scroll_y < -len(self.credits) * 35:
                self.scroll_y = self.height

            for i, line in enumerate(self.credits):
                self.draw_text(line, self.font, WHITE, self.screen, self.width // 2, int(self.scroll_y + i * 35))

            pygame.display.flip()
            self.clock.tick(60)
            await asyncio.sleep(0)
