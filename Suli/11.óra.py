class Alkalmazott:
    def __init__(self, nev, id, fizetes, reszleg):
        self.nev = nev
        self.id = id
        self.fizetes = fizetes
        self.reszleg = reszleg
    def fizuszamol(self, fizetes, ledolgozott_ora):
        tulora = 0
        if ledolgozott_ora > 50:
            tulora = ledolgozott_ora - 50
        self.fizetes = self.fizetes + (tulora * (self.fizetes/50))
    def reszlegcser(self, alk_reszleg):
        self.reszleg = alk_reszleg
    def adatkiir(self):
        print('----------------------------')
        print(f"\n Név: ", self.nev)
        print(f"\n ID: ", self.id)
        print(f"\n Fizetés: ", self.fizetes)
        print(f"\n Részleg: ", self.reszleg)
        print('----------------------------')
"""
alkalmazott1 = Alkalmazott("Ádám", "A1", 200000 , "Marketing")
alkalmazott2 = Alkalmazott("Béla", "B1",200000, "Sales")
alkalmazott3 = Alkalmazott("Csaba", "C1",200000, "IT")
alkalmazott4 = Alkalmazott("Dani", "D1",200000, "Vezetőség")

print(alkalmazott1.adatkiir())
print(alkalmazott2.adatkiir())
print(alkalmazott3.adatkiir())
print(alkalmazott4.adatkiir())

alkalmazott1.reszlegcser("IT")
print(alkalmazott1.reszleg)
alkalmazott2.fizuszamol(250000, 52)
print(alkalmazott2.fizetes)
"""

class Etterem:
    def __init__(self):
        self.menu_elemek = {}
        self.asztal_foglalas = []
        self.rendelesek = []
    def menu_felvisz(self, etel, ar):
        self.menu_elemek[etel] = ar
    def foglalasok(self, asztal_szam):
        self.asztal_foglalas.append(asztal_szam)
    def etlap_kiir(self):
        for etel, ar in self.menu_elemek.itemes():
            print(f"{etel}: {ar}")

etterem1 = Etterem()

etterem1.menu_felvisz("Hamburger", 1000)
etterem1.menu_felvisz("Pizza", 1500)
etterem1.menu_felvisz("Cola", 500)

etterem1.foglalasok(1)
