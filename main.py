import pygame
import pygame.mixer 
from personagem import *
from fantasma import * 
from colisao import * 
from telas import *

class Game:
    def __init__(self, width=900, height=500):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Angry Birds")
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.personagem = Personagem()
        self.fantasma1 = Fantasma([350, 100])
        self.fantasma2 = Fantasma([200, 150])
        self.colisao = Colisao()
        self.telas = Telas(width, height)
        self.personagens_coletados = 0 
        self.personagens_totais = 6

    def iniciar_musica(self):
        pygame.mixer.music.load('musica/som.mp3')
        pygame.mixer.music.play(-1)
        
    def run(self):
        self.iniciar_musica()
        while self.running:
            dt = self.clock.tick(60) / 1000  
            self._handle_events()
            self._update(dt)
            self._draw()
            
    def verifica_vitoria(self):
        if self.personagens_coletados == self.personagens_totais:
            self.telas.estado_atual = "venceu"
    
    def verifica_perda(self):
        if self.tentativas_restantes <= 0:
            self.telas.estado_atual = "gameover"

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.telas.handle_event(event) 
            if self.telas.estado_atual == "jogo":
                self.personagem.handle_event(event)


    def _update(self, dt):       
        if self.telas.estado_atual == "jogo":
            self.fantasma1.atualiza_aceleracao(self.personagem)
            self.fantasma2.atualiza_aceleracao(self.personagem)
            self.personagem.update(dt)
            if self.colisao.verificar_colisao(self.personagem.imagem.get_rect(topleft=self.personagem.pos)):
                self.personagem.reset_pos()
                self.personagens_coletados += 1
                self.verifica_vitoria()
    def _draw(self):
        self.screen.fill((255, 255, 255))
        self.telas.draw(self.screen) 
        if self.telas.estado_atual == "jogo":
            self.personagem.draw(self.screen)
            self.colisao.desenhar(self.screen)
            self.fantasma1.desenha_corpo(self.screen)
            self.fantasma2.desenha_corpo(self.screen)
        pygame.display.flip()


    def quit(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
    game.quit()