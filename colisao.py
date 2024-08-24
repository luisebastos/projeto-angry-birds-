import pygame 

class Colisao():
    def __init__(self):
        self.caixa = pygame.transform.scale(pygame.image.load('assets/caixa angry birds.png'), (70, 70))
        self.posicoes = [(570, 350), (670, 350), (770, 350), (620, 270), (720, 270), (670, 190)]
        self.caixas = [self.caixa.get_rect(topleft = pos) for pos in self.posicoes]
        self.personagens = [
            {'imagem': pygame.transform.scale(pygame.image.load('assets/olaf.png'), (50, 70)), 'pos': (570, 350)},
            {'imagem': pygame.transform.scale(pygame.image.load('assets/dumbo.png'), (50, 70)), 'pos': (675, 350)},
            {'imagem': pygame.transform.scale(pygame.image.load('assets/stitch.png'), (50, 70)), 'pos': (770, 350)},
            {'imagem': pygame.transform.scale(pygame.image.load('assets/pooh.png'), (50, 70)), 'pos': (630, 270)},
            {'imagem': pygame.transform.scale(pygame.image.load('assets/moana_pig.png'), (50, 70)), 'pos': (720, 270)},
            {'imagem': pygame.transform.scale(pygame.image.load('assets/boo.png'), (50, 70)), 'pos': (670, 190)}
        ]
        self.caixas = [self.caixa.get_rect(topleft=pos) for pos in self.posicoes]
        self.personagem_rects = [pygame.Rect(personagem['pos'], (50, 70)) for personagem in self.personagens]
            
        
    def desenhar(self, screen):
        for caixa, personagem in zip(self.caixas, self.personagens):
            screen.blit(self.caixa, caixa.topleft)
            screen.blit(personagem['imagem'], personagem['pos'])
            
            
    def verificar_colisao(self, personagem_rect):              
        for i, caixa in enumerate(self.caixas[:]):
            if personagem_rect.colliderect(caixa):
                self.caixas.pop(i)
                self.personagem_rects.pop(i)
                self.personagens.pop(i)
                
                
 
 
 