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
def melyseg():
    sor_szam, oszlop_szam, melyseg_adatok = beolvas_fajl('melyseg.txt')
    sor_index = int(input(f"Kérjük, adja meg a sor azonosítóját (1-{sor_szam}): "))
    oszlop_index = int(input(f"Kérjük, adja meg az oszlop azonosítóját (1-{oszlop_szam}): "))
    melyseg(sor_index, oszlop_index, melyseg_adatok)

feladat(3)
feladat(4)
feladat(5)
feladat(6)

