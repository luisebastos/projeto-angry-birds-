import pygame
import numpy as np

class Personagem():
    def __init__(self):
        self.s0 = np.array([50, 370], dtype=float)
        self.pos = self.s0.copy()
        self.imagem = pygame.transform.scale(pygame.image.load('assets/amarelo_angry.png'), (55, 77))
        self.v = np.array([0, 0], dtype=float)
        self.dragging = False
        self.initial_pos = None
        self.gravidade = np.array([0, 2.7])
        
        
    def normaliza(self, vf, forca):
        mod = np.linalg.norm(vf)
        if mod != 0:
            return (vf / mod) * forca
        return np.array([0, 0])


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.dragging = True
            self.initial_pos = np.array(pygame.mouse.get_pos(), dtype=float)
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.dragging:
                final_pos = np.array(pygame.mouse.get_pos(), dtype=float)
                vf = self.initial_pos - final_pos
                self.v = self.normaliza(vf, 250)  
            self.dragging = False
    
    
    def update(self, dt):
        if not self.dragging:
            if self.pos not in self.s0: 
                self.v = self.v + self.gravidade
            self.pos += self.v * dt * 2


    def draw(self, screen):
        screen.blit(self.imagem, self.pos)
        if self.dragging and self.initial_pos is not None:
            pygame.draw.line(screen, (255, 0, 0), self.initial_pos, pygame.mouse.get_pos(), 5)
        
        
            
    
        