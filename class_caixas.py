class Caixas: 
    def __init__(self, image, posicao_inicial):
        self.image = image
        self.rect = self.image.get_rect(center=posicao_inicial)
        self.visivel = True 

    def desenhar (self, tela):
        if self.visivel:
            tela.blit(self.image, self.rect.topleft)
        
    def colisao_caixa(self, personagem_rect):
        if self.rect.colliderect(personagem_rect):
            self.visivel = False
            
                