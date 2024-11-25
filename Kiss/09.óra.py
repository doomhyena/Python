from asyncio import new_event_loop


class Osztály:
    i = 10

o1 = Osztály()

print(o1.i)

class Kutya:
    def ugat(self):
        print("Vaú")

kutya1 = Kutya()

print(kutya1.ugat())

class Kutya2:
    def __init__(self, nev):
        self.nev = nev
k1 = Kutya2("Francia Bulldog")
k2 = Kutya2("Cane Corso")

print(k1.nev)
print(k2.nev)

class Macska:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor
    def nevlekerdezes(self):
        return self.nev

m = Macska("Boldizsár", 5)

print(m.nevlekerdezes())

print(f"A macska neve {m.nev}, a kora pedig {m.kor} év.")

class Alkalmazott:
    def __init__(self, nev, kor, fizetes):
        self.nev = nev
        self.kor = kor
        self.fizetes = fizetes
    def lekerdezes(self):
        return self.nev

alk = Alkalmazott("Kovács János", 35, 250000)


print(f"A nevem {alk.nev}, {alk.kor} vagyok, {alk.fizetes}FT keresek.")

class Tanulo:
    def __init__(self, id, nev, evfolyam, kepzes):
        self.id = id
        self.nev = nev
        self.evfolyam = evfolyam
        self.kepzes = kepzes
    def lekerdezes(self):
        return self.nev

tanulo = Tanulo(4, "Csontos Kincső", 13, "Szoftverfejlesztő- és Tesztelő")

print(f" {tanulo.id} -> {tanulo.nev}, {tanulo.evfolyam} évfolyamba jár, és {tanulo.kepzes}-nak/nek tanul.")
