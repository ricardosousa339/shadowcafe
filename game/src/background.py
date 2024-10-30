import pygame

class Background:
    def __init__(self, width, height):
        
                # Dicionário de fundos
        backgrounds = {
            "cafeteria_4": "game/src/assets/cafeteria/imagem_4luzes.png",
            "cafeteria_3": "game/src/assets/cafeteria/imagem_3luzes.png",
            "cafeteria_2": "game/src/assets/cafeteria/imagem_2luzes.png",
            "cafeteria_1": "game/src/assets/cafeteria/imagem_1luz.png",
            "cafeteria_0": "game/src/assets/cafeteria/imagem_normal.png",
        }
        self.backgrounds = {name: pygame.transform.scale(pygame.image.load(path).convert(), (width, height)) for name, path in backgrounds.items()}

        
        self.current_background = list(self.backgrounds.keys())[0]  # Define o primeiro fundo como o atual

    def set_background(self, name):
        if name in self.backgrounds:
            self.current_background = name

    def draw(self, screen):
        screen.blit(self.backgrounds[self.current_background], (0, 0))