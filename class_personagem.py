import pygame 

class Personagem:
    def __init__(self, imagem, posicao_inicial):
        self.image = imagem
        self.rect = self.image.get_rect(center=posicao_inicial)
    
    def desenhar_personagem(self, tela):
        tela.blit(self.image, self.rect.topleft)
        pygame.display.update()

    def atualizar(self):
        self.mover()
        pygame.display.update()
        
        