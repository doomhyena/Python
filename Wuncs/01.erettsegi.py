def feladat(n):
    print(f"{n}.feladat: ")

feladat(1)

hetek_szam = str(input("Kérek egy hét számot: "))
testtomeg = float(input("Elérni kívánt testtömeg (kg): "))

kg = testtomeg

feladat(2)

def hetek(n):
    print(f"{n}. héten: ")

while (testtomeg != kg):
    hetek(1) + 1
    hetek = float(input(f"{hetek(1)} "))

else:
    print(f"Mari néni a(z) {hetek(1)} héten érte el a célt.")
