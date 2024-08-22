import pygame
import numpy as np
import random

pygame.init()

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0)
COR_PERSONAGEM = (30, 200, 20)
COR_ATRATOR_1 = (200, 30, 30)
COR_ATRATOR_2 = (30, 30, 200)

# Definir as posições dos dois corpos celestes
sol_1 = np.array([150, 200])
sol_2 = np.array([250, 200])

G = 5000

# Função para gerar as pedras
def gera_pedras(num_pedras):
    pedras = []
    for i in range(num_pedras):
        # Metade das partículas orbitam o primeiro corpo celeste
        if i < num_pedras // 2:
            pos = np.array([random.uniform(50, 150), random.uniform(100, 300)], dtype=np.float64)
            vel = np.array([0.0, random.uniform(-7, 7)], dtype=np.float64)
        # A outra metade orbita o segundo corpo celeste
        else:
            pos = np.array([random.uniform(250, 350), random.uniform(100, 300)], dtype=np.float64)
            vel = np.array([0.0, random.uniform(-7, 7)], dtype=np.float64)

        pedras.append({
            'pos': pos,
            'vel': vel
        })
    return pedras

# Número de pedras
num_pedras = 50

# Inicializar as pedras
pedras = gera_pedras(num_pedras)

# Personagem (pedra)
personagem = pygame.Surface((5, 5))
personagem.fill(COR_PERSONAGEM)

rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Atualizar posições e velocidades das pedras
    for pedra in pedras:
        d_vec_1 = sol_1 - pedra['pos']
        d_1 = np.linalg.norm(d_vec_1)

        d_vec_2 = sol_2 - pedra['pos']
        d_2 = np.linalg.norm(d_vec_2)

        if d_1 > 0:
            a1 = (G / d_1**2) * (d_vec_1 / d_1)
        else:
            a1 = np.array([0, 0], dtype=np.float64)

        if d_2 > 0:
            a2 = (G / d_2**2) * (d_vec_2 / d_2)
        else:
            a2 = np.array([0, 0], dtype=np.float64)


        a = a1 + a2

        pedra['vel'] += a
        pedra['pos'] += 0.1 * pedra['vel']

    # Desenhar fundo
    screen.fill(BLACK)

    # Desenhar os dois atratores
    pygame.draw.circle(screen, COR_ATRATOR_1, sol_1.astype(int), 10)
    pygame.draw.circle(screen, COR_ATRATOR_2, sol_2.astype(int), 10)

    # Desenhar todas as pedras
    for pedra in pedras:
        rect = pygame.Rect(pedra['pos'], (10, 10))
        screen.blit(personagem, rect)

    # Atualizar a tela
    pygame.display.update()

    # Controlar frame rate
    clock.tick(FPS)

# Terminar tela
pygame.quit()
