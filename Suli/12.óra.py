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
