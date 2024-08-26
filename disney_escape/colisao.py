import pygame 
import os

class Colisao():
    def __init__(self):
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        olaf = os.path.join(base_path, 'assets', 'olaf.png')
        dumbo = os.path.join(base_path, 'assets', 'dumbo.png')
        stitch = os.path.join(base_path, 'assets', 'stitch.png')
        pooh = os.path.join(base_path, 'assets', 'pooh.png')
        moana_pig = os.path.join(base_path, 'assets', 'moana_pig.png')
        boo = os.path.join(base_path, 'assets', 'boo.png')
        caixa = os.path.join(base_path, 'assets', 'caixa angry birds.png')
        
        self.caixa = pygame.transform.scale(pygame.image.load(caixa), (85, 85))
        self.posicoes = [(570, 300), (670, 300), (770, 300), (620, 220), (720, 220), (670, 140)]
        self.caixas = [self.caixa.get_rect(topleft = pos) for pos in self.posicoes]
        
        self.personagens = [
            {'imagem': pygame.transform.scale(pygame.image.load(olaf), (60, 70)), 'pos': (580, 300)},
            {'imagem': pygame.transform.scale(pygame.image.load(dumbo), (55, 60)), 'pos': (690, 310)},
            {'imagem': pygame.transform.scale(pygame.image.load(stitch), (60, 70)), 'pos': (780, 310)},
            {'imagem': pygame.transform.scale(pygame.image.load(pooh), (50, 55)), 'pos': (635, 235)},
            {'imagem': pygame.transform.scale(pygame.image.load(moana_pig), (60, 70)), 'pos': (740, 225)},
            {'imagem': pygame.transform.scale(pygame.image.load(boo), (60, 70)), 'pos': (680, 150)}
        ]
        self.caixas = [self.caixa.get_rect(topleft=pos) for pos in self.posicoes]
        self.personagem_rects = [pygame.Rect(personagem['pos'], (50, 70)) for personagem in self.personagens]

        self.personagens_conquistados = [(10 + i * 70, 10) for i in range(6)]
        self.conquistados = []
            
        
    def desenhar(self, screen):
        for caixa, personagem in zip(self.caixas, self.personagens):
            screen.blit(self.caixa, caixa.topleft)
            screen.blit(personagem['imagem'], personagem['pos'])
        
        for personagem in self.conquistados:
            screen.blit(personagem['imagem'], personagem['pos'])
            
            
    def verificar_colisao(self, personagem_rect):              
        for i, caixa in enumerate(self.caixas[:]):
            if personagem_rect.colliderect(caixa):
                self.caixas.pop(i)
                personagem_conquistado = self.personagens.pop(i)
                self.personagem_rects.pop(i)

                nova_posicao = (10 + len(self.conquistados) * 70, 10)  
                personagem_conquistado['pos'] = nova_posicao

                self.conquistados.append(personagem_conquistado)
                return True  
        return False  
                    
                
 
 
 