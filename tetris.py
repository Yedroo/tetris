import pygame, sys,os
from pygame.locals import *

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


wzor_szer = 5
wzor_wys = 5
okno_szer = 320
okno_wys = 240
plansza_wys = 20
plansza_szer = 10
puste = '.'
rozm_kwadratu = 5
marg_x = int((okno_szer - plansza_wys * rozm_kwadratu) / 2)
gorny_margines = okno_wys - (plansza_wys * rozm_kwadratu) - 1

zielony = (0, 155, 0)
czarny = (0, 0, 0)
niebieski = (0, 0, 155)
kolor = zielony

okno_gry = pygame.display.set_mode((okno_szer, okno_wys))

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
                    'y': -2}
    return nowy_element

def przeksztalc_na_pixel(boxx, boxy):
    return (marg_x + (boxx * rozm_kwadratu)), (gorny_margines + (boxy * rozm_kwadratu))

def rysuj_kwadrat(boxx, boxy, color, pixelx=None, pixely=None):
    if color == puste:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = przeksztalc_na_pixel(boxx, boxy)
        pygame.draw.rect(okno_gry, kolor, (pixelx+1, pixely+1, rozm_kwadratu-1, rozm_kwadratu -1))

def rysuj_plansze(plansza):
    #rysuje border wokół planszy
    pygame.draw.rect(okno_gry, czarny, marg_x -3, gorny_margines -7, (plansza_szer * rozm_kwadratu) +8, (plansza_wys * rozm_kwadratu)+8, 5 )
    #ponoć wypełnia tło
    pygame.draw.rect(okno_gry, niebieski, (marg_x, gorny_margines, rozm_kwadratu * plansza_szer, rozm_kwadratu * plansza_wys))
    #ma rysować pojedyncze kwadraty z elementów
    for x in range (plansza_szer):
        for y in range(plansza_szer):
            rysuj_kwadrat(x, y, plansza[x, y])

def rysuj_element(element, pixelx=None, pixely=None):
    ksztalt_do_rysowania = ksztalty[element['ksztalt']]
    if pixelx == None and pixely == None:
        pixelx, pixely = przeksztalc_na_pixel(element['x'], element['y'])

    for x in range(wzor_szer):
        for y in range(wzor_wys):
            if ksztalt_do_rysowania[y][x] != puste:
                rysuj_kwadrat(None, None, element['color'], pixelx + (x * rozm_kwadratu), pixely + (y*rozm_kwadratu))
                
def main():
    pygame.init()

# def input(events):
#   for event in events:
#      if event.type == QUIT:
#         sys.exit(0)

# while True:
#   input(pygame.event.get())
