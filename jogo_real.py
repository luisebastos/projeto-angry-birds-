import pygame
from class_personagem import *

class game:
    # Inicializa o jogo
    def __init__(self, width=800, height=450):
        pygame.init()
        pygame.display.set_caption('Angry Birds')
        
        self.screen = pygame.display.set_mode((width, height))
        self.BLACK = (0, 0, 0)
        
        self.rodando = True
        self.jogo_iniciado = False
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        
        self.assets = {
            'angry_birds': pygame.transform.scale(pygame.image.load('assets/amarelo_angry.png'), (55, 77))
        }
                
        posicao_inicial = (width // 2, height // 2)  # Posição inicial do personagem no centro da tela
        self.personagem = Personagem(self.assets['angry_birds'], posicao_inicial)
        
    def tela_inicial(self): 
        while not self.jogo_iniciado: 
            self.screen.fill(self.BLACK)
            font = pygame.font.SysFont(None, 55)
            texto = font.render("Pressione qualquer tecla para começar", True, self.WHITE)
            self.screen.blit(texto, (self.screen.get_width() // 2 - texto.get_width() // 2, self.screen.get_height() // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False
                    self.jogo_iniciado = True  # Para sair do loop
                if event.type == pygame.KEYDOWN:
                    self.jogo_iniciado = True
        
    # Processa eventos do jogo
    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False

    # Desenha na tela
    def desenhar(self):
        self.screen.fill(self.BLACK)
        self.personagem.desenhar_personagem(self.screen)  # Desenha o personagem na telad
        pygame.display.update()

    # Loop principal do jogo
    def rodar(self):
        self.tela_inicial()
        while self.rodando:
            self.processar_eventos()
            self.desenhar()
        
        pygame.quit()

if __name__ == "__main__":
    jogo = game()
    jogo.rodar()



