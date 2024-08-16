import pygame
from class_personagem import *

class game:
    # Inicializa o jogo
    def __init__(self, width=900, height=500):
        pygame.init()
        pygame.display.set_caption('Angry Birds')
        
        self.screen = pygame.display.set_mode((width, height))
        self.BLACK = (0, 0, 0)
        
        self.rodando = True
        self.jogo_iniciado = False
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        
        self.assets = {
            'tela_inicial': pygame.transform.scale(pygame.image.load('assets/menu.png'), (width, height)), 
            'tela_jogo': pygame.transform.scale(pygame.image.load('assets/jogo_inicio.png'), (width, height)),
            'angry_birds_amarelo': pygame.transform.scale(pygame.image.load('assets/amarelo_angry.png'), (55, 77))
        }
                
        posicao_inicial = (width // 2, height // 2)  # Posição inicial do personagem no centro da tela
        self.personagem = Personagem(self.assets['angry_birds_amarelo'], posicao_inicial)
        self.clicar_iniciar_jogo = pygame.Rect(150, height - 150, 120, 120)
        self.clicar_instrucoes_jogo = pygame.Rect(650, height - 150, 120, 120) #CRIAR TELA DE INSTRUCOES PARA IMPLEMENTAR ISSO
        
    def tela_inicial(self): 
        while not self.jogo_iniciado: 
            self.screen.blit(self.assets['tela_inicial'], (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False
                    self.jogo_iniciado = True  # Para sair do loop
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.clicar_iniciar_jogo.collidepoint(event.pos):
                        self.jogo_iniciado = True
        
    # Processa eventos do jogo
    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False

    # Desenha na tela
    def desenhar(self):
        self.screen.blit(self.assets['tela_jogo'], (0, 0))
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



