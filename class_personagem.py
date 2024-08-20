import pygame 

class Personagem:
    def __init__(self, imagem, posicao_inicial):
        self.image = imagem
        self.rect = self.image.get_rect(center=posicao_inicial)
        self.selecionado = False
        self.visivel = True 
        self.posicao_fora = [0, 0]  
        
    def desenhar_personagem(self, tela):
        if self.visivel:  
            tela.blit(self.image, self.rect.topleft)

    def atualizar(self):
        if self.selecionado and self.visivel: 
            self.rect.center = pygame.mouse.get_pos()

    def colisao_personagem(self, outro_rect):
        if self.visivel and self.rect.colliderect(outro_rect):
            self.rect.topleft = tuple(self.posicao_fora)

