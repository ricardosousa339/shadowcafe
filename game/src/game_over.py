import pygame

class GameOverScreen:
    def __init__(self, screen, width, height, acucar, cafe):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font("game/src/assets/fonts/goblin.otf", 14)
        self.font2 = pygame.font.Font("game/src/assets/fonts/homevideo.ttf", 50)
        
        mensagem_1 = ""
        mensagem_2 = "☕"
        mensagem_3 = ""
        mensagem_4 = "CAFÉ       - {}".format(cafe)
        mensagem_5 = "AÇÚCAR  - {}".format(acucar)
        
        
        if acucar > cafe:
            mensagem_1 = "DE AMARGA JÁ BASTA A VIDA!"
            mensagem_3 = "Você perdeu com doçura!"
        elif cafe > acucar:
            mensagem_1 = "A VIDA É DURA, MAS O CAFÉ É FORTE!"
            mensagem_3 = "Você perdeu com força!"
        else:
            mensagem_1 = "NA VIDA, COMO NO CAFÉ:   EQUILÍBRIO É TUDO." 
            mensagem_3 = "Você perdeu!"
        
        self.text1 = self.font.render(mensagem_1, True, (255, 255, 255))
        self.text2 = self.font2.render(mensagem_2, True, (255, 255, 255))
        self.text3 = self.font.render(mensagem_3, True, (255, 255, 255))
        self.text4 = self.font.render(mensagem_4, True, (255, 255, 255))
        self.text5 = self.font.render(mensagem_5, True, (255, 255, 255))
        
        skin = "game/src/assets/game_over/lightcafe.png"
        if acucar > cafe:
            skin = "game/src/assets/game_over/cafedoce.png"
        elif cafe > acucar:
            skin = "game/src/assets/game_over/cafeforte.png"
        
        self.image = pygame.image.load(skin).convert_alpha()
        
        
        self.image = pygame.transform.scale(self.image, (200, 200))  # Redimensionar a imagem para caber na tela
        
        self.button_font = pygame.font.Font("game/src/assets/fonts/homevideo.ttf", 30)       
        self.button_text = self.button_font.render("▶️ Reiniciar", True, (255, 255, 255))
        self.button_padding = 20
        self.button_rect = pygame.Rect(
            self.width // 2 - self.button_text.get_width() // 2 - self.button_padding,
            self.height - 100 - self.button_padding,
            self.button_text.get_width() + 2 * self.button_padding,
            self.button_text.get_height() + 2 * self.button_padding
        )
        
    def show(self):
        self.screen.fill((6, 2, 37))
        self.screen.blit(self.image, (self.width // 2 - self.image.get_width() // 2, 50))  # Desenhar a imagem de game over
        self.screen.blit(self.text1, (self.width // 2 - self.text1.get_width() // 2, 300))
        self.screen.blit(self.text2, (self.width // 2 - self.text2.get_width() // 2, 350))        
        self.screen.blit(self.text3, (self.width // 2 - self.text3.get_width() // 2, 450))
        pygame.draw.line(self.screen, (255, 255, 255), (50, 500), (self.width -50, 500), 2)
        
        self.screen.blit(self.text4, (300, 550))
        self.screen.blit(self.text5, (300, 600))
        
        pygame.draw.rect(self.screen, (0, 51, 102), self.button_rect)
        button_text_x = self.button_rect.x + (self.button_rect.width - self.button_text.get_width()) // 2
        button_text_y = self.button_rect.y + (self.button_rect.height - self.button_text.get_height()) // 2
        self.screen.blit(self.button_text, (button_text_x, button_text_y))
        
        pygame.display.flip()

        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    return False  
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: 
                        game_over = False
                        return True 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        game_over = False
                        return True