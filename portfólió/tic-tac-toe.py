import pygame
import sys

pygame.init()

FEHER = (255, 255, 255)
FEKETE = (0, 0, 0)
KEK = (0, 0, 255)
PIROS = (255, 0, 0)

SZEL, MAG = 300, 300
KEPERNYO = pygame.display.set_mode((SZEL, MAG))
pygame.display.set_caption("Tic Tac Toe")

XO = "X"  
jatekter = [["" for _ in range(3)] for _ in range(3)]
jatekos_nyert = False

betutipus = pygame.font.SysFont(None, 75)

def kirajzol(jatekos):
    szoveg = betutipus.render(jatekos + " nyert!", True, KEK if jatekos == "X" else PIROS)
    KEPERNYO.blit(szoveg, (SZEL // 4, MAG // 2 - 50))
    pygame.display.update()
    pygame.time.delay(2000)

def racs():
    KEPERNYO.fill(FEHER)
    pygame.draw.line(KEPERNYO, FEKETE, (SZEL / 3, 0), (SZEL / 3, MAG), 5)
    pygame.draw.line(KEPERNYO, FEKETE, (SZEL * 2 / 3, 0), (SZEL * 2 / 3, MAG), 5)
    pygame.draw.line(KEPERNYO, FEKETE, (0, MAG / 3), (SZEL, MAG / 3), 5)
    pygame.draw.line(KEPERNYO, FEKETE, (0, MAG * 2 / 3), (SZEL, MAG * 2 / 3), 5)

def kirajzol_XO():
    for i in range(3):
        for j in range(3):
            if jatekter[i][j] == "X":
                szoveg = betutipus.render("X", True, KEK)
                KEPERNYO.blit(szoveg, (j * SZEL / 3 + 30, i * MAG / 3 + 10))
            elif jatekter[i][j] == "O":
                szoveg = betutipus.render("O", True, PIROS)
                KEPERNYO.blit(szoveg, (j * SZEL / 3 + 30, i * MAG / 3 + 10))

def ellenoriz_gyoztes():
    global jatekos_nyert

    for sor in range(3):
        if jatekter[sor][0] == jatekter[sor][1] == jatekter[sor][2] != "":
            kirajzol(jatekter[sor][0])
            jatekos_nyert = True
    for oszlop in range(3):
        if jatekter[0][oszlop] == jatekter[1][oszlop] == jatekter[2][oszlop] != "":
            kirajzol(jatekter[0][oszlop])
            jatekos_nyert = True
    if jatekter[0][0] == jatekter[1][1] == jatekter[2][2] != "":
        kirajzol(jatekter[0][0])
        jatekos_nyert = True
    if jatekter[0][2] == jatekter[1][1] == jatekter[2][0] != "":
        kirajzol(jatekter[0][2])
        jatekos_nyert = True

def kezeli_kattintas(x, y):
    global XO

    oszlop = x // (SZEL // 3)
    sor = y // (MAG // 3)

    if jatekter[sor][oszlop] == "":
        jatekter[sor][oszlop] = XO
        XO = "O" if XO == "X" else "X"
        ellenoriz_gyoztes()

def jatek():
    global jatekos_nyert
    racs()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not jatekos_nyert:
                x, y = pygame.mouse.get_pos()
                kezeli_kattintas(x, y)
                racs()
                kirajzol_XO()
        pygame.display.update()

jatek()
