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
feladat(5)
feladat(6)

