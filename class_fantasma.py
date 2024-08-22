import numpy as np

class Fantasma:
    def __init__(self, imagem, posicao_inicial):
        self.imagem = imagem
        self.rect = self.imagem.get_rect(center=posicao_inicial)

    def gravidade(self, personagem):
        G = 100
        d_vec = np.array(personagem.rect.center) - np.array(self.rect.center)
        d = np.linalg.norm(d_vec)

        if d > 0 and d < 150:  
            a = (G / d**2) * (d_vec / d)
            personagem.velocidade += a 
        else:
            a = np.array([0, 0], dtype=np.float64)

        return a

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)
