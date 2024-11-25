'''
1. feladat:

Készítsünk egy Zeneszerzo osztályt.
Tulajdonságok: a neve, az országa és a műfaj amien alkot
Az osztály tartsa szamon a generált példányok szamát
Az ország tulajdonság 'OrszágNév Régióként' tárolja

'''

def feladat(n):
    print(f"{n}.feladat: ")

feladat(1)

class Zeneszerzo:
    példányok_szama = 0

    def __init__(self, név, ország, műfaj):
        self.név = név
        self.ország = f"{ország} Régió"
        self.műfaj = műfaj
        Zeneszerzo.példányok_szama += 1

    @classmethod
    def példányok_szama_megtekintése(cls):
        return cls.példányok_szama


zs1 = Zeneszerzo("Bach", "Németország", "Barokk")
zs2 = Zeneszerzo("Mozart", "Ausztria", "Klasszikus")

print(Zeneszerzo.példányok_szama_megtekintése())

'''
2.feladat:

Legyen egy szamoló osztály, amihez egy darab szamot kell megadni példányosításkor.
Az alapján generál magának három új tulajdonságot: egyesek, hármasok kilencesek.
Mindhárom tulajdonság azt a szamot tárolja tartalomként, ahány egésszer megvan naz adott szam a beírt értékben.
Pl.: 12 esetén 12, 4 és egy lesz a tulajdonság tartalma
Segédfüggvény? egy sablonmondat megfogalmazza, hogy melyik szam hány egésszer van meg az adott példány esetén

'''

feladat(2)

class Szamolo:
    def __init__(self, szam):
        self.szam = szam
        self.egyesek = 1
        self.hármasok = 3
        self.kilencesek = 9

    def sablonmondat(self):
        return f"A(z) {self.szam} számban az egyes {int(self.szam / self.egyesek)}-szer szerepel benne, a három {int(self.szam / self.hármasok)}-szer szerepel benne és a klenc {int(self.szam / self.kilencesek)}-szer szerepel."

s = Szamolo(12)

print(s.sablonmondat())

'''

3.feladat: 
Kaja osztály 3 paraméterrel: név, kedvenc ételeek listája és nem kedveltek listája
Plusz egy segédfüggvény, ami kiírja, hogy emberünk mit eszik és szereti-e

'''

feladat(3)

class Kaja:
    def __init__(self, nev, kedvenc_etelek, nem_kedveltek):
        self.nev = nev
        self.kedvenc_etelek = kedvenc_etelek
        self.nem_kedveltek = nem_kedveltek

    def eszik(self):
        print(f"{self.nev} eszik: {self.kedvenc_etelek}")
        print(f"{self.nev} nem kedveltek: {self.nem_kedveltek}")
