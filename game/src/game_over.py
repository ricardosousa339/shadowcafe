import pygame

class GameOverScreen:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 74)
        self.text = self.font.render("Game Over", True, (255, 0, 0))
        
        self.image = pygame.image.load('game/assets/game_over/lightcafe.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))  # Redimensionar a imagem para caber na tela
        
        
    def show(self):
        self.screen.fill((6, 2, 37))
        self.screen.blit(self.image, (self.width // 2 - self.image.get_width() // 2, 0))
        self.screen.blit(self.text, (self.width // 2 - self.text.get_width() // 2, self.height // 2 - self.text.get_height() // 2))
        pygame.display.flip()

        # Loop para manter a tela de fim de jogo até ser fechada
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    return False  # Indica que o jogo deve ser encerrado
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Pressionar Enter para reiniciar o jogo
                        game_over = False
                        return True  # Indica que o jogo deve ser reiniciado