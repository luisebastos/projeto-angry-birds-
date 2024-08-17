import pygame
from class_personagem import *
from class_fantasma import *
from class_caixas import *


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
            'angry_birds_amarelo': pygame.transform.scale(pygame.image.load('assets/amarelo_angry.png'), (55, 77)),
            'angry_birds_vermelho': pygame.transform.scale(pygame.image.load('assets/vermelho_angry.png'), (55, 77)),
            'angry_birds_azul': pygame.transform.scale(pygame.image.load('assets/azul_angry.png'), (55, 77)),
            'angry_birds_rosa': pygame.transform.scale(pygame.image.load('assets/rosa_angry.png'), (55, 77)),
            'angry_birds_preto': pygame.transform.scale(pygame.image.load('assets/preto_angry.png'), (55, 77)),
            'angry_birds_branco': pygame.transform.scale(pygame.image.load('assets/branco_angry.png'), (55, 77)),
            'boo': pygame.transform.scale(pygame.image.load('assets/boo.png'), (75, 80)),
            'olaf': pygame.transform.scale(pygame.image.load('assets/olaf.png'), (60, 75)),
            'moana': pygame.transform.scale(pygame.image.load('assets/moana.png'), (80, 85)),
            'dumbo': pygame.transform.scale(pygame.image.load('assets/dumbo.png'), (65, 65)),
            'pooh': pygame.transform.scale(pygame.image.load('assets/pooh.png'), (65, 65)),
            'stitch': pygame.transform.scale(pygame.image.load('assets/stitch.png'), (75, 80)),
            'caixa': pygame.transform.scale(pygame.image.load('assets/caixa angry birds.png'), (85, 85)),
            'fantasma': pygame.transform.scale(pygame.image.load('assets/fantasma.png'), (75, 80)),
        }

        # adicionando musica 
        pygame.mixer.music.load('musica/som.mp3')
        pygame.mixer.music.play() 
                
        posicao_inicial = (width // 2, height // 2)  # Posição inicial do personagem no centro da tela
        self.personagem = Personagem(self.assets['angry_birds_amarelo'], posicao_inicial)
        self.personagens_adicionais = [
            Personagem(self.assets['boo'], (670, 190)),
            Personagem(self.assets['olaf'], (570, 350)),
            Personagem(self.assets['dumbo'], (670, 350)),
            Personagem(self.assets['moana'], (720, 270)),
            Personagem(self.assets['stitch'], (770, 350)),
            Personagem(self.assets['pooh'], (620, 270)),
        ]

        self.fantasma = Fantasma(self.assets['fantasma'], (100, 100))
        self.fantasma2 = Fantasma(self.assets['fantasma'], (200, 200))
        
        self.clicar_iniciar_jogo = pygame.Rect(150, height - 150, 120, 120)
        self.clicar_instrucoes_jogo = pygame.Rect(550, height - 150, 150, 150) # Área clicável para instruções
        self.clicar_back_instrucoes = pygame.Rect(100, height - 150, 120, 120)


        posicoes_caixas = [(570, 350), (670, 350), (770, 350), (620, 270), (720, 270), (670, 190)]
        self.caixas = [Caixas(self.assets['caixa'], pos) for pos in posicoes_caixas]
        
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
        
        for caixa in self.caixas:
            caixa.colisao_caixa(self.personagem.rect)


    def desenhar(self):
        self.screen.blit(self.assets['tela_jogo'], (0, 0))
        self.personagem.atualizar()  # Atualiza a posição do personagem
        self.personagem.desenhar_personagem(self.screen)  # Desenha o personagem na tela

        for personagem in self.personagens_adicionais: # personagens da disney
            personagem.desenhar_personagem(self.screen)
        
        self.fantasma.desenhar(self.screen) # obstaculo
        self.fantasma2.desenhar(self.screen) 

        for caixa in self.caixas: # CAIXAS
            caixa.desenhar(self.screen)

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
