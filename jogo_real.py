import pygame
from class_personagem import *

class Game:
    def __init__(self, width=900, height=500):
        pygame.init()
        pygame.display.set_caption('Angry Birds')
        
        self.screen = pygame.display.set_mode((width, height))
        self.BLACK = (0, 0, 0)
        
        self.rodando = True
        self.estado = 'inicial'  
        
        self.assets = {
            'tela_inicial': pygame.transform.scale(pygame.image.load('assets/menu.png'), (width, height)), 
            'tela_jogo': pygame.transform.scale(pygame.image.load('assets/jogo_inicio.png'), (width, height)),
            'tela_instrucoes': pygame.transform.scale(pygame.image.load('assets/instrucoes.png'), (width, height)),
            'angry_birds_amarelo': pygame.transform.scale(pygame.image.load('assets/amarelo_angry.png'), (55, 77))
        }
                
        posicao_inicial = (width // 2, height // 2)  # Posição inicial do personagem no centro da tela
        self.personagem = Personagem(self.assets['angry_birds_amarelo'], posicao_inicial)
        self.clicar_iniciar_jogo = pygame.Rect(150, height - 150, 120, 120)
        self.clicar_instrucoes_jogo = pygame.Rect(550, height - 150, 150, 150) # Área clicável para instruções
        self.clicar_back_instrucoes = pygame.Rect(100, height - 150, 120, 120)
        
    def tela_inicial(self): 
        while self.estado == 'inicial': 
            self.screen.blit(self.assets['tela_inicial'], (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False
                    self.estado = 'sair'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.clicar_iniciar_jogo.collidepoint(event.pos):
                        self.estado = 'jogo'
                    elif self.clicar_instrucoes_jogo.collidepoint(event.pos):
                        self.estado = 'instrucoes'
    
    
    def tela_instrucoes(self):
        while self.estado == 'instrucoes':
            self.screen.blit(self.assets['tela_instrucoes'], (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False
                    self.estado = 'sair'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.clicar_back_instrucoes.collidepoint(event.pos):
                        self.estado = 'inicial'
    
    
    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.personagem.rect.collidepoint(event.pos):
                    self.personagem.selecionado = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.personagem.selecionado = False


    def desenhar(self):
        self.screen.blit(self.assets['tela_jogo'], (0, 0))
        self.personagem.atualizar()  # Atualiza a posição do personagem
        self.personagem.desenhar_personagem(self.screen)  # Desenha o personagem na tela
        pygame.display.update()


    def rodar(self):
        while self.rodando:
            if self.estado == 'inicial':
                self.tela_inicial()
            elif self.estado == 'instrucoes':
                self.tela_instrucoes()
            elif self.estado == 'jogo':
                self.processar_eventos()
                self.desenhar()
        
        pygame.quit()


if __name__ == "__main__":
    jogo = Game()
    jogo.rodar()
