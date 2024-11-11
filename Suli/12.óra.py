class BankAdatok:
    def __init__(self, bankszamlaszam, nyitas_datum, egyenleg, ugyfelnev):
        self.bankszamlaszam = bankszamlaszam
        self.nyitas_datum = nyitas_datum
        self.egyenleg = egyenleg
        self.ugyfelnev = ugyfelnev
    def berak(self, osszeg):
        self.egyenleg += osszeg
        print(f"{osszeg} lett berakva.")
    def kivesz(self, osszeg):
        if osszeg > self.egyenleg:
            print("Nincs elég pénzed!")
        else:
            self.egyenleg -= osszeg
            print(f"{osszeg} lett levéve a bankszámládról.")
    def egyenleg_lekerdezes(self):
        print(f'A jelenlegi egyenleg {self.egyenleg}')
    def reszlet_kiir(self):
        print(f"\nNév: {self.nev}")
        print(f"\nSzámlaszám: {self.bankszamlaszam}")
        print(f"\nNyitás dátuma: {self.nyitas_datum}")
        print(f"\nEgyenleg: {self.egyenleg}")

class Leltar:
    def __init__(self):
        self.leltar = {}
    def hozzaad(self, id, megnevezes, darabszam, ar):
        self.leltar[id] = {"Termék neve":megnevezes, "Darabaszám":darabszam, "Ár":ar}
    def modosit(selfself, id, darabszam, ar):
        if id in self.leltar:
            self.leltar[id]["Darabszám"] = darabszam
            self.leltar[id]["Ár"] = ar
        else:
            print("Nem található a keresett termék. ")