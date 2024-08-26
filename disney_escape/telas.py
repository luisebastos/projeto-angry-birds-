import pygame 
import os

class Telas: 
    def __init__(self, width=900, height=500): 
        
        base_path = os.path.dirname(os.path.abspath(__file__))
        menu = os.path.join(base_path, 'assets', 'menu.png')
        instrucoes = os.path.join(base_path, 'assets', 'instrucoes.png')
        venceu = os.path.join(base_path, 'assets', 'venceu.png')
        gameover = os.path.join(base_path, 'assets', 'gameover.png')
        jogo_inicio = os.path.join(base_path, 'assets', 'jogo_inicio.png')
        
        self.tela_inicial = pygame.transform.scale(pygame.image.load(menu), (width, height))
        self.tela_instrucoes = pygame.transform.scale(pygame.image.load(instrucoes), (width, height))
        self.tela_venceu = pygame.transform.scale(pygame.image.load(venceu), (width, height))
        self.tela_gameover = pygame.transform.scale(pygame.image.load(gameover), (width, height))
        self.tela_jogo = pygame.transform.scale(pygame.image.load(jogo_inicio), (width, height))
        self.botao_jogar = pygame.Rect(150, height - 150, 120, 120)
        self.botao_instrucoes = pygame.Rect(550, height - 150, 150, 150)
        self.clicar_back_instrucoes = pygame.Rect(100, height - 150, 120, 120)
        self.estado_atual = "inicio"
        
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.estado_atual == "inicio":
                if self.botao_jogar.collidepoint(event.pos): 
                    self.estado_atual = "jogo"
                if self.botao_instrucoes.collidepoint(event.pos):
                    self.estado_atual = "instrucao"
            elif self.estado_atual == "instrucao":
                if self.clicar_back_instrucoes.collidepoint(event.pos): 
                    self.estado_atual = "inicio"
            

    def draw(self, window): 
        if self.estado_atual == "inicio":
            window.blit(self.tela_inicial, (0, 0))
        elif self.estado_atual == "instrucao":
            window.blit(self.tela_instrucoes, (0, 0))
        elif self.estado_atual == "jogo":
            window.blit(self.tela_jogo, (0, 0))
        elif self.estado_atual == "venceu":
            window.blit(self.tela_venceu, (0, 0))
        elif self.estado_atual == "gameover":
            window.blit(self.tela_gameover, (0, 0))
            
            