import pygame
import time
import random

pygame.init()

feher = (255, 255, 255)
fekete = (0, 0, 0)
piros = (213, 50, 80)
zold = (0, 255, 0)
kek = (50, 153, 213)

szelesseg, magassag = 600, 400
kepernyo = pygame.display.set_mode((szelesseg, magassag))
pygame.display.set_caption('Snake Játék')

kigyomeret = 10
sebesseg = 15

betutipus = pygame.font.SysFont("bahnschrift", 25)
score_betutipus = pygame.font.SysFont("comicsansms", 35)

def pontszam(pont):
    ertek = score_betutipus.render("Pontszám: " + str(pont), True, kek)
    kepernyo.blit(ertek, [0, 0])

def kigyo(kigyomeret, kigyo_test):
    for x in kigyo_test:
        pygame.draw.rect(kepernyo, fekete, [x[0], x[1], kigyomeret, kigyomeret])

def uzenet(msg, szin):
    szoveg = betutipus.render(msg, True, szin)
    kepernyo.blit(szoveg, [szelesseg / 6, magassag / 3])

def jatek():
    jatek_vege = False
    jatek_leallt = False

    x = szelesseg / 2
    y = magassag / 2

    x_valtozas = 0
    y_valtozas = 0

    kigyo_test = []
    kigyo_hossza = 1

    etel_x = round(random.randrange(0, szelesseg - kigyomeret) / 10.0) * 10.0
    etel_y = round(random.randrange(0, magassag - kigyomeret) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not jatek_vege:

        while jatek_leallt:
            kepernyo.fill(feher)
            uzenet("Vesztettél! Nyomj Q-t a kilépéshez vagy C-t az újrakezdéshez", piros)
            pontszam(kigyo_hossza - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        jatek_vege = True
                        jatek_leallt = False
                    if event.key == pygame.K_c:
                        jatek()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jatek_vege = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_valtozas = -kigyomeret
                    y_valtozas = 0
                elif event.key == pygame.K_RIGHT:
                    x_valtozas = kigyomeret
                    y_valtozas = 0
                elif event.key == pygame.K_UP:
                    y_valtozas = -kigyomeret
                    x_valtozas = 0
                elif event.key == pygame.K_DOWN:
                    y_valtozas = kigyomeret
                    x_valtozas = 0

        if x >= szelesseg or x < 0 or y >= magassag or y < 0:
            jatek_leallt = True

        x += x_valtozas
        y += y_valtozas
        kepernyo.fill(feher)
        pygame.draw.rect(kepernyo, zold, [etel_x, etel_y, kigyomeret, kigyomeret])
        
        kigyo_fej = []
        kigyo_fej.append(x)
        kigyo_fej.append(y)
        kigyo_test.append(kigyo_fej)
        
        if len(kigyo_test) > kigyo_hossza:
            del kigyo_test[0]

        for szegmens in kigyo_test[:-1]:
            if szegmens == kigyo_fej:
                jatek_leallt = True

        kigyo(kigyomeret, kigyo_test)
        pontszam(kigyo_hossza - 1)

        pygame.display.update()

        if x == etel_x and y == etel_y:
            etel_x = round(random.randrange(0, szelesseg - kigyomeret) / 10.0) * 10.0
            etel_y = round(random.randrange(0, magassag - kigyomeret) / 10.0) * 10.0
            kigyo_hossza += 1

        clock.tick(sebesseg)

    pygame.quit()
    quit()

jatek()
