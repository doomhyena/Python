def feladat(n):
    print(f"{n}. feladat")

feladat(1)

class Konyvtar:
    def __init__(self, cim, iro, oldalszam, megjelenesev):
        self.cim = cim
        self.iro = iro
        self.oldalszam = oldalszam
        self.megjelenesev = megjelenesev

    def konyvadatok(self):
        print(f"{self.cim} könyv {self.oldalszam} oldalas és {self.iro} írta.")

    def tagolt(self, adat):
        cim, iro, oldalszam, megjelenesev = adat.split(".")
        return Konyvtar(cim, iro, int(oldalszam), int(megjelenesev))

    def klasszikuse(self):
        if self.megjelenesev <= 1900:
            print("A mű klasszikus.")
        else:
            print('A mű nem klasszikus.')

konyv = Konyvtar("A Gyűrűk Ura", "J.R.R. Tolkien", 1216, 1954)
konyv.konyvadatok()
konyv.klasszikuse()

feladat(2)

class Nev:
    def __init__(self, vezeteknev, keresztnev, eletkor):
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        self.eletkor = eletkor
        self.teljesnev = f"{vezeteknev} {keresztnev}"

    def monogram(self):
        print(f"Monogram: {self.vezeteknev[0]}. {self.keresztnev[0]}.")

    def kor(self):
        if self.eletkor > 18:
            print(f"{self.teljesnev} már nagykorú!")
        else:
            print(f"{self.teljesnev} még kiskorú")

    def kiiras(self):
        return f"{self.teljesnev}, {self.eletkor} éves."

nev = Nev("Csontos", "Kincső", 19)
nev.monogram()
nev.kor()

feladat(3)

class Szamsor:
    def __init__(self):
        self.szamlista = []

    def felvisz(self, szam):
        if szam:
            self.szamlista.append(szam)
        else:
            print("Kérlek, adj meg egy számot!")

    def kiiras(self):
        return self.szamlista

szamsor = Szamsor()

szamsor.felvisz(5)
szamsor.felvisz(10)
szamsor.felvisz(3.5)

print(szamsor.kiiras())
