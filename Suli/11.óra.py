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

