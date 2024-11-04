"""class Tanulo:
    def __init__(self, id, nev, evfolyam, kepzes):
        self.id = id
        self.nev = nev
        self.evfolyam = evfolyam
        self.kepzes = kepzes
    def lekerdezes(self):
        return self.nev
    def tagolt(adat):
        id, nev, evfolyam, kepzes = (adat).split("/")
        return Tanulo(id, nev, evfolyam, kepzes)

tanulo = Tanulo(4, "Csontos Kincső", 13, "Szoftverfejlesztő- és Tesztelő")
tt = Tanulo.tagolt("04-Kincső-13-Szoftverfejlesztő- és Tesztelő")

#print(tt)
print(f" {tanulo.id} -> {tanulo.nev}, {tanulo.evfolyam} évfolyamba jár, és {tanulo.kepzes}-nak/nek tanul.")"""


class Beteg:
    def __init__(self, szig, nev, panasz, diagnozis):
        self.szig = szig
        self.nev = nev
        self.panasz = panasz
        self.diagnozis = diagnozis
    def kiiras(self):
        return f"{Beteg.nev} beteget {Beteg.panasz} panasszal hozták be és kiderült, hogy {Beteg.diagnozis}-e van."
    def tagolt(adat):
        szig, nev, panasz, diagnozis = (adat).split("/")
        return Beteg(szig, nev, panasz, diagnozis)

#b = Beteg.tagolt('1-Béla-Hasfájás-Gyomorrontás')
#print(b.panasz)

