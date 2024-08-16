import pygame

class SimpleScreen:
    def __init__(self, width=900, height=500):
        pygame.init()
        pygame.display.set_caption('Angry Birds')
        
        
        # Configurações da tela
        self.screen = pygame.display.set_mode((width, height))
        self.BLACK = (0, 0, 0)
        self.start_screen_image = pygame.image.load("assets/menu.png")
        
        self.rodando = True

    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False

    def desenhar(self):
        self.screen.blit(self.start_screen_image, (0, 0))
        pygame.display.update()

    def rodar(self):
        while self.rodando:
            self.processar_eventos()
            self.desenhar()
        
        pygame.quit()

if __name__ == "__main__":
    jogo = SimpleScreen()
    jogo.rodar()



