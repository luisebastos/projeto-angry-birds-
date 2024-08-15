import pygame

class SimpleScreen:
    def __init__(self, width=800, height=450):
        pygame.init()
        pygame.display.set_caption('Angry Birds')
        
        # Configurações da tela
        self.screen = pygame.display.set_mode((width, height))
        self.BLACK = (0, 0, 0)
        
        self.rodando = True

    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False

    def desenhar(self):
        self.screen.fill(self.BLACK)
        pygame.display.update()

    def rodar(self):
        while self.rodando:
            self.processar_eventos()
            self.desenhar()
        
        pygame.quit()

if __name__ == "__main__":
    jogo = SimpleScreen()
    jogo.rodar()



