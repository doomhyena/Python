class Tanulo:
    def __init__(self, id, nev, evfolyam, kepzes):
        self.id = id
        self.nev = nev
        self.evfolyam = evfolyam
        self.kepzes = kepzes
    def lekerdezes(self):
        return self.nev

tanulo = Tanulo(4, "Csontos Kincső", 13, "Szoftverfejlesztő- és Tesztelő")

# print(f" {tanulo.id} -> {tanulo.nev}, {tanulo.evfolyam} évfolyamba jár, és {tanulo.kepzes}-nak/nek tanul.")

def tagolt(adat):
    id, nev, evfolyam, kepzes = (adat).split("/")
    return Tanulo(id, nev, evfolyam, kepzes)

tt = Tanulo.tagolt("04/Csontos Kincső/13/Szoftverfejlesztő- és Tesztelő")

# print(tt)