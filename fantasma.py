import pygame
import numpy as np

class Fantasma():
    def __init__(self, pos_inicial):
        self.pos = np.array(pos_inicial, dtype=float) 
        self.massa = 90000 
        self.raio_influencia = 200
        self.imagem = pygame.transform.scale(pygame.image.load('assets/fantasma.png'), (70, 70))
    
    
    def atualiza_aceleracao(self, personagem):
        direcao = self.pos - personagem.pos
        distancia = np.linalg.norm(direcao)
        if distancia < self.raio_influencia and distancia > 0:
            direcao_normalizada = direcao / distancia   
            forca = (self.massa / (distancia**2))
            aceleracao = direcao_normalizada * forca
            personagem.v += aceleracao

    
    def desenha_corpo(self, screen):
        screen.blit(self.imagem, self.pos)
        
        
        