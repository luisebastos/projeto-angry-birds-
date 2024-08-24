import pygame 

class Telas: 
    def __init__(self, width=900, height=500): 
        self.tela_inicial = pygame.transform.scale(pygame.image.load('assets/menu.png'), (width, height))
        self.tela_instrucoes = pygame.transform.scale(pygame.image.load('assets/instrucoes.png'), (width, height))
        self.tela_venceu = pygame.transform.scale(pygame.image.load('assets/venceu.png'), (width, height))
        self.tela_gameover = pygame.transform.scale(pygame.image.load('assets/gameover.png'), (width, height))
        self.tela_jogo = pygame.transform.scale(pygame.image.load('assets/jogo_inicio.png'), (width, height))
        self.botao_jogar = pygame.Rect(150, height - 150, 120, 120)
        self.botao_instrucoes = pygame.Rect(550, height - 150, 150, 150)
        self.botao_jogar_novamente = pygame.Rect(315, height - 150, 120, 120)
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
            elif self.estado_atual == "venceu":
                if self.botao_jogar_novamente.collidepoint(event.pos): 
                    self.estado_atual = "jogo"
            


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
            
            