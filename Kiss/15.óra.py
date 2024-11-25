def feladat(n):
    print(f"{n}.feladat")

feladat(1)

fajlnev = 'melyseg.txt'

def beolvas_fajl(fajlnev):
    with open(fajlnev, 'r') as f:
        sorok = f.readlines()
    sor_szam = int(sorok[0].strip())
    oszlop_szam = int(sorok[1].strip())

    melyseg_adatok = []
    for i in range(2, 2 + sor_szam):
        melyseg_adatok.append(list(map(int, sorok[i].strip().split())))
    return sor_szam, oszlop_szam, melyseg_adatok


def beolvas():
    sor_szam, oszlop_szam, melyseg_adatok = beolvas_fajl('melyseg.txt')
    print(f"Összes sor: {sor_szam}, Összes oszlop: {oszlop_szam}")
    for sor in melyseg_adatok:
        print(sor)

feladat(2)

def kiir_melyseg(sor_index, oszlop_index, melyseg_adatok):
    melyseg = melyseg_adatok[sor_index - 1][oszlop_index - 1]
    print(f"A {sor_index}. sor {oszlop_index}. oszlopában mért mélység: {melyseg} dm")

feladat(3)

def terulet_es_atlagos_melyseg(melyseg_adatok):
    terulet = 0
    osszes_melyseg = 0
    osszes_pont = 0

    for sor in melyseg_adatok:
        for melyseg in sor:
            if melyseg > 0:
                terulet += 1
                osszes_melyseg += melyseg
                osszes_pont += 1

    atlagos_melyseg = osszes_melyseg / osszes_pont if osszes_pont > 0 else 0
    return terulet, atlagos_melyseg

feladat(4)
def legnagyobb_melyseg(melyseg_adatok):
    max_melyseg = 0
    max_pontok = []

    for i in range(len(melyseg_adatok)):
        for j in range(len(melyseg_adatok[i])):
            if melyseg_adatok[i][j] > max_melyseg:
                max_melyseg = melyseg_adatok[i][j]
                max_pontok = [(i + 1, j + 1)]
            elif melyseg_adatok[i][j] == max_melyseg:
                max_pontok.append((i + 1, j + 1))

    return max_melyseg, max_pontok

feladat(5)

def partvonal_hossza(melyseg_adatok):
    hossza = 0
    sorok = len(melyseg_adatok)
    oszlopok = len(melyseg_adatok[0])

    for i in range(sorok):
        for j in range(oszlopok):
            if melyseg_adatok[i][j] > 0:
                if i == 0 or melyseg_adatok[i - 1][j] == 0:
                    hossza += 1
                if i == sorok - 1 or melyseg_adatok[i + 1][j] == 0:
                    hossza += 1
                if j == 0 or melyseg_adatok[i][j - 1] == 0:
                    hossza += 1
                if j == oszlopok - 1 or melyseg_adatok[i][j + 1] == 0:
                    hossza += 1

    return hossza

feladat(6)

def sávdiagram(oszlop_index, melyseg_adatok):
    with open('diagram.txt', 'w') as f:
        for i in range(len(melyseg_adatok)):
            melyseg = melyseg_adatok[i][oszlop_index - 1]
            meter_melyseg = round(melyseg / 10)
            f.write(f"{i + 1:02d} {'*' * meter_melyseg}\n")
