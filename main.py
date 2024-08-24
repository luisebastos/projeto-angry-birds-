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
        self.fantasma = Fantasma()
        self.colisao = Colisao()
        self.telas = Telas(width, height)
        
        
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
            

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.telas.handle_event(event) 
            if self.telas.estado_atual == "jogo":
                self.personagem.handle_event(event)


    def _update(self, dt):
        if self.telas.estado_atual == "jogo":
            self.fantasma.atualiza_aceleracao(self.personagem)
            self.personagem.update(dt)
            self.colisao.verificar_colisao(self.personagem.imagem.get_rect(topleft=self.personagem.pos))


    def _draw(self):
        self.screen.fill((255, 255, 255))
        self.telas.draw(self.screen) 
        if self.telas.estado_atual == "jogo":
            self.personagem.draw(self.screen)
            self.colisao.desenhar(self.screen)
            self.fantasma.desenha_corpo(self.screen)
        pygame.display.flip()


    def quit(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
    game.quit()