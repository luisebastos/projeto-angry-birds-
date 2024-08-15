
import math
import matplotlib.pyplot as plt
import numpy as np
import pygame
from pygame.locals import *
pygame.init()

def main():
    # Tamanho da tela e definição do FPS
    pygame.display.set_caption('Angry Birds')
    screen = pygame.display.set_mode((800, 450))
    clock = pygame.time.Clock()
    FPS = 60  # Frames per Second

    BLACK = (0, 0, 0)
    COR_PERSONAGEM = (30, 200, 20)

        # Inicializar posicoes
    s0 = np.array([200,200])
    v = np.array([-1, -1])
    s = s0

        # Personagem
    personagem = pygame.Surface((5, 5))  # Tamanho do personagem
    personagem.fill(COR_PERSONAGEM)  # Cor do personagem

    rodando = True
    while rodando:
            # Capturar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            # Controlar frame rate
    clock.tick(FPS)

            # Processar posicoes
    y = pygame.mouse.get_pos()
    v = y - s
    s = s + v * 5 / np.linalg.norm(v)

            # Desenhar fundo
    screen.fill(BLACK)

            # Desenhar personagem
    rect = pygame.Rect(s, (10, 10))  # First tuple is position, second is size.
    screen.blit(personagem, rect)

            # Update!
    pygame.display.update()

        # Terminar tela
    pygame.quit()