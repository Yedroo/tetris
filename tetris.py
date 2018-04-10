import pygame, sys,os
from pygame.locals import *


wzor_szer = 5
wzor_wys = 5

s_ksztalt_wzor = [[ '.....',
                    '.....',
                    '..XX.',
                    '.XX..',
                    '.....'],
                  [ '.....',
                    '..X..',
                    '..XX.',
                    '...X.',
                    '.....']]

z_ksztalt_wzor = [[ '.....',
                    '.....',
                    '.XX..',
                    '..XX.',
                    '.....'],
                  [ '.....',
                    '..X..',
                    '.XX..',
                    '.X...',
                    '.....']],

i_ksztalt_wzor = [[ '..X..',
                    '..X..',
                    '..X..',
                    '..X..',
                    '.....'],
                  [ '.....',
                    '.....',
                    'XXXX.',
                    '.....',
                    '.....']]

o_ksztalt_wzor = [ '.....',
                    '.....',
                    '.XX..',
                    '.XX..',
                    '.....']

j_ksztalt_wzor = [[ '.....',
                    '..X..',
                    '..X..',
                    '.XX..',
                    '.....'],
                  [ '.....',
                    '.X...',
                    '.XXX.',
                    '.....',
                    '.....'],
                  [ '.....',
                    '..XX.',
                    '..X..',
                    '..X..',
                    '.....'],
                  [ '.....',
                    '.....',
                    '.XXX.',
                    '...X.',
                    '.....']]

l_ksztalt_wzor = [[ '.....',
                    '..X..',
                    '..X..',
                    '..XX.',
                    '.....'],
                  [ '.....',
                    '.....',
                    '.XXX.',
                    '.X...',
                    '.....'],
                  [ '.....',
                    '.XX..',
                    '..X..',
                    '..X..',
                    '.....'],
                  [ '.....',
                    '...X.',
                    '.XXX.',
                    '.....',
                    '.....']]

t_ksztalt_wzor = [[ '.....',
                    '.XXX.',
                    '..X..',
                    '.....',
                    '.....'],
                  [ '.....',
                    '..X..',
                    '.XX..',
                    '..X..',
                    '.....'],
                  [ '.....',
                    '..X..',
                    '.XXX.',
                    '.....',
                    '.....'],
                  [ '.....',
                    '..X..',
                    '..XX.',
                    '..X..',
                    '.....']]

ksztalty = {'S': s_ksztalt_wzor,
            'Z': z_ksztalt_wzor,
            'J': j_ksztalt_wzor,
            'L': l_ksztalt_wzor,
            'I': i_ksztalt_wzor,
            'O': o_ksztalt_wzor,
            'T': t_ksztalt_wzor}

okno_szer = 320
okno_wys = 240
plansza_wys = 20
plansza_szer = 10
puste = '.'

zielony = (0, 155, 0)
kolor = zielony

def dodaj_plansze():
    plansza = []
    for i in range(plansza_szer):
        plansza.append([puste] * plansza_wys)
    return plansza

def dodaj_nowy_element():
    ksztalt = random.choice(list(ksztalty.keys()))
    nowy_element = {'ksztalt': ksztalt,
                    'obrot': random.randint(0, len(ksztalty[ksztalt]) - 1),
                    'x': int(gra_szer/2 - okno_szer/2),
                    'y': -2,
                    'kolor': kolor}
    return nowy_element

def dodaj_na_plansze(plansza, element):
    for x in range(wzor_szer):
        for y in range(wzor_wys):
            if ksztalty[element['shape']][element['rotation']][x][y] != puste:
                plansza[x + element['x']][y + element['y']] = element['kolor']

def main():
    pygame.init()
    okno_gry = pygame.display.set_mode((320, 240))

# def input(events):
#   for event in events:
#      if event.type == QUIT:
#         sys.exit(0)

# while True:
#   input(pygame.event.get())

