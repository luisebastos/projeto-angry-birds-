import pygame
import math
pygame.init()



#a função cria pokemons no dict assets, cria a tela, muda o ícone e o nome da janela. No dict 'state', tem todas as informações que o jogo vai utilizar, como as caixas, quantidade das bolinhas, a física do jogo, etc. O dict 'pokemon' guarda cada pokemon numa caixa e suas respectivas posições. A função também cria as bolinhas.
def inicializa():
    
    assets = {
        'brock' : pygame.image.load("docs/imagens/personagem.png"), 
        'caixa' : pygame.image.load("docs/imagens/caixa angry birds.png"),
        'estilingue' : pygame.image.load("docs/imagens/estilingue.png"),
        'bulbasaur' : pygame.image.load("docs/imagens/planta dino.png"), 
        'clefairy' : pygame.image.load("docs/imagens/clefairy.png"),
        'estrelinha' : pygame.image.load("docs/imagens/estrelinha.png"),
        'eevee' : pygame.image.load("docs/imagens/leaozinho.png"), 
        'pikachu' : pygame.image.load("docs/imagens/pikachu.png"), 
        'mimikyu' : pygame.image.load("docs/imagens/mimikyu.png"),
        'pokebola' : pygame.image.load("docs/imagens/pokebola.png"),
        'exclamação' : pygame.image.load("docs/imagens/exclamação.png"),
        'snorlax' : pygame.image.load("docs/imagens/snorlax.png"),
        'fofopreto' : pygame.image.load("docs/imagens/cachorro].png"),
        'rosinha' : pygame.image.load("docs/imagens/meufav.png"),
        'rato' : pygame.image.load("docs/imagens/sato.png"),
        'enfeite1' : pygame.image.load("docs\imagens\enfeite1.png")
    }

    pygame.display.set_caption('PokeSlingshot')
    pygame.display.set_icon(pygame.image.load("docs/imagens/icone.png"))
    window = pygame.display.set_mode((1000, 450), vsync=True, flags=pygame.SCALED)
    pygame.mixer.music.load("docs/musica/sound.mp3")
    pygame.mixer.music.play() 
    state = {
        'teta' : 0,
        'vel_x' : 0,
        'vel_y' : 0,
        'atirou' : False,
        'pos_y_mira' : 20,
        'vel_mira': 4,
        'bolinha_pos' : [],
        'caixas' : [(800, 285), (860, 285), (920, 285), (830, 226), (890, 226), (860, 167), (580, 285), (520, 285), (548, 226), (310, 285)],
        'lista_rect' : [],
        'max_bolinhas': 20,
        'texto_bolinhas': 20,
        'pos_x_livre': 70,
        'tela' : 1
    }


    pokemon = {
                   # caixa       #pokemon
        'rato' : [(310, 285), [319, 295]], 
        'fofopreto' : [(520, 285), [528,295]], 
        'snorlax' : [(580, 285), [587,285]],
        'rosinha': [(548, 226), [563,235]],
        'estrelinha': [(800, 285), [810,297]],
        'bulbasaur': [(860, 285), [865, 289]],
        'clefairy': [(920, 285), [925, 289]], 
        'eevee': [(830, 226),[843, 234]],
        'pikachu': [(890, 226), [886, 233]],
        'mimikyu': [(860, 167), [870, 173]]
    }

    state['pokemon'] = pokemon

    for pos in state['caixas']:
        state['lista_rect'].append(pygame.Rect(pos[0], pos[1], 50, 50)) 
    
    for i in range(20): 
        state['bolinha_pos'].append([110, 325]) 

    return window, assets, state


# a função desenha os objetos na janela, desenha as diversas telas, como de início, gameover e de parabéns por conseguir completar o jogo
def desenha(window, assets, state):
    if state['tela'] == 1:
        window.blit(pygame.image.load("docs/imagens/tela iniciar instruções.png"), (0,0))

    elif state['tela'] == 2: 
        window.blit(pygame.image.load("docs/imagens/instruções.png"), (0,0))  

    #aqui a tela 3 é a tela do jogo, onde todos os objetos e física acontecerão
    elif state['tela'] == 3: 

        #transforma a escala dos objetos/figuras
        fundo_jogo = pygame.image.load("docs/imagens/download.png")
        fundo_jogo = pygame.transform.scale(fundo_jogo, (1000, 450))
        assets['brock'] = pygame.transform.scale(pygame.image.load("docs/imagens/personagem.png"), (120,120))
        assets['caixa'] = pygame.transform.scale(assets['caixa'], (60, 60))
        assets['estilingue'] = pygame.transform.scale(assets['estilingue'], (30,50)) 
        assets['bulbasaur'] = pygame.transform.scale(assets['bulbasaur'], (50,50))
        assets['clefairy'] = pygame.transform.scale(assets['clefairy'], (55,55))
        assets['estrelinha'] = pygame.transform.scale(assets['estrelinha'], (40,45))
        assets['eevee'] = pygame.transform.scale(assets['eevee'], (45,45))
        assets['pikachu'] = pygame.transform.scale(assets['pikachu'], (70,50))
        assets['mimikyu'] = pygame.transform.scale(assets['mimikyu'], (45,45))
        assets['pokebola'] = pygame.transform.scale(assets['pokebola'], (15,15))
        assets['exclamação'] = pygame.transform.scale(assets['exclamação'], (45,45))
        assets['snorlax'] = pygame.transform.scale(assets['snorlax'], (50,50))
        assets['fofopreto'] = pygame.transform.scale(assets['fofopreto'], (45,45))
        assets['rosinha'] = pygame.transform.scale(assets['rosinha'], (40,40))
        assets['rato'] = pygame.transform.scale(assets['rato'], (40,40))
        assets['enfeite1'] = pygame.transform.scale(assets['enfeite1'], (70,40))

        #define a posição dos pokemons e das figuras na tela
        window.blit(fundo_jogo, (0,0)) 
        window.blit(assets['bulbasaur'], (state['pokemon']['bulbasaur'][1]))
        window.blit(assets['brock'], ((5, 250)))
        window.blit(assets['estilingue'], ((100, 320)))
        window.blit(assets['clefairy'], (state['pokemon']['clefairy'][1]))
        window.blit(assets['estrelinha'], (state['pokemon']['estrelinha'][1]))
        window.blit(assets['eevee'], ((state['pokemon']['eevee'][1])))
        window.blit(assets['pokebola'], (state['bolinha_pos'][0])) 
        window.blit(assets['pikachu'], (state['pokemon']['pikachu'][1]))
        window.blit(assets['mimikyu'], (state['pokemon']['mimikyu'][1]))
        window.blit(assets['exclamação'], ((40, 210)))
        window.blit(assets['snorlax'], (state['pokemon']['snorlax'][1]))
        window.blit(assets['fofopreto'], (state['pokemon']['fofopreto'][1]))
        window.blit(assets['rosinha'], (state['pokemon']['rosinha'][1]))
        window.blit(assets['rato'], (state['pokemon']['rato'][1]))
        window.blit(assets['enfeite1'], (85, 40))
        window.blit(assets['enfeite1'], (95, 70))

        #desenha a barra de força e a mira
        vermelho = pygame.draw.rect(window, (255,0,0), (14.3, 16, 25, 114.7))
        amarelo = pygame.draw.rect(window, (255,255,0), (14.3, 130, 25, 67.1))
        verde = pygame.draw.rect(window, (0, 128,0), (14.3, 180, 25, 45.7))
        mira = pygame.draw.rect(window, (0,0,0), (17,state['pos_y_mira'], 40,4))  
        
        #desenha o texto da quantidade de pokebolas para serem lançadas 
        fonte = pygame.font.SysFont('Arial', 20, bold=True)
        texto = fonte.render(str(state['texto_bolinhas']), True, (0,0,0))
        texto_x = 110
        texto_y = 370
        window.blit(texto, (texto_x, texto_y))


        for i in state['caixas']:
            window.blit(assets['caixa'], (i))

    elif state['tela'] == 4:
        window.blit(pygame.image.load("docs\imagens\gameover.png"), (0,0))

    elif state['tela'] == 5:
        window.blit(pygame.image.load("docs\imagens\parabens.png"), (0,0)) 

    pygame.display.update()

def recebe_eventos(state): 
        #tela 1: tela de início
        if state['tela'] == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    #se o usuário clicar em 'iniciar', o jogo começa
                    if 127 <= event.pos[0] <= 127 + 291 and 129 <= event.pos[1] <= 129 + 110:
                        state['tela'] = 3 
                    #se o usuário clicar em 'instruções', vai para a tela 2 (instruções)
                    if 605 <= event.pos[0] <= 605 + 320 and 134 <= event.pos[1] <= 134 + 98:
                        state['tela'] = 2 
        elif state['tela'] == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #botão de voltar para a tela inicial
                    if 0 <= event.pos[0] <= 0 + 163 and 0 <= event.pos[1] <= 0 + 61: 
                        state['tela'] = 1
        #aqui a mira tem uma determinada coordenada para não sair da barra de força e inverte a velocidade quando atinge o limite
        elif state['tela'] == 3:      
                if state['pos_y_mira'] < 20 or state['pos_y_mira'] >= 218:
                    state['vel_mira'] *= (-1)
                state['pos_y_mira'] += state['vel_mira']
                vel_x = 0
                if state['bolinha_pos'][0][1] > 450:
                    del state['bolinha_pos'][0] 
                    state['atirou'] = False
                
                index = -1 
                #aqui verifica se a bolinha colidiu com a caixa
                if len(state['bolinha_pos']) > 0:  
                    index = pygame.Rect(state['bolinha_pos'][0][0], state['bolinha_pos'][0][1], 15, 15).collidelist(state['lista_rect']) 
                   
                #caixas 
                #se colidiu com as caixas, remove a bolinha e as caixas da lista que elas estão
                if index != -1:
                    for poke in state['pokemon'].values():
                        if state['caixas'][index] == poke[0]:
                            state['pos_x_livre'] += 70
                            poke[1][0] = state['pos_x_livre']
                            poke[1][1] = 370
                    del state['caixas'][index]
                    del state['lista_rect'][index] 
                    del state['bolinha_pos'][0]
                    state['atirou'] = False

                if len(state['caixas']) == 0:
                    state['tela'] = 5 

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    #física do jogo
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        state['vel_x'] = 50*(state['pos_y_mira'] - 225.7) / -209.7
                        state['vel_y'] = -40 * math.sin(45)
                        state['atirou'] = True
                        state['texto_bolinhas'] -= 1
                        #se a quantidade de bolinhas for 0 e todas as caixas forem atingidas, o jogador vence
                        if state['texto_bolinhas'] <= -1 and len(state['caixas']) == 0:
                            state['tela'] = 5
                        #se as pokebolas acabarem e ainda existirem caixas na tela, o jogador perde e vai para a tela de gameover
                        elif state['texto_bolinhas'] <= -1 and len(state['caixas']) != 0:
                            state['tela'] = 4 

                #verifica a física do jogo
                if state['atirou']:
                    state['bolinha_pos'][0][0] += state['vel_x']
                    state['vel_y'] += 2 
                    state['bolinha_pos'][0][1] += state['vel_y']
                if len(state['bolinha_pos']) == 0: 
                    if len(state['caixas']) == 0:
                        state['tela'] = 5
                    else:
                        state['tela'] = 4 
 
        elif state['tela'] == 4:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False 

        elif state['tela'] == 5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False 
                     
        return True