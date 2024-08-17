import pygame 

class Personagem:
    def __init__(self, imagem, posicao_inicial):
        self.image = imagem
        self.rect = self.image.get_rect(center=posicao_inicial)
        self.selecionado = False
    
    def desenhar_personagem(self, tela):
        tela.blit(self.image, self.rect.topleft)

    def atualizar(self):
        if self.selecionado:
            self.rect.center = pygame.mouse.get_pos()
