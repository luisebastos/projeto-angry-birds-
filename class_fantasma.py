class Fantasma:
    def __init__(self, imagem, posicao_inicial):
        self.imagem = imagem
        self.rect = self.imagem.get_rect(center=posicao_inicial)

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect.topleft)