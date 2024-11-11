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

