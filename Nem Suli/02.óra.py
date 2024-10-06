# változók

i = 5

# Nem kell típusokat megadni, a Python maga eldönti.

# Ez egy függvény

"""

def metódusnév(paraméterek):
    műveletek
    return eredmény


"""

## Példa

def faktorialis(szam):
    megoldas = 1
    for i in range(szam):
        megoldas *= i+1
    return megoldas

print(faktorialis(5))

print("---")

# Ciklusok

"""

For ciklus: Adott művelet ismétlése egy tartományban. range() adja meg, meddig fusson.
While ciklus: Addig fut, amíg egy feltétel igaz.

"""

## Példa

for i in range(5):
    print(i)

print("---")

# Feltételek
# If-else: Eldönti, melyik kód fusson egy feltétel alapján.

szam = 0

if szam == 0:
    print("Ez nulla!")
else:
    print("Ez nem nulla!")

print("---")

# Listák (Tömbök)
# A lista több elemet tartalmazhat, sorszámmal érhetők el az elemek.

lista = [4, 5, 1, 3]
print(lista[0])  # első elem kiírása

print("---")

def legnagyobb(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

print(legnagyobb([16, 2, 5, 7, 10, 1, 3, 6, 8, 4]))

print("---")

def mhszamol(szo):
    maganhangzok = "aeiou"
    osszesen = 0
    for betu in szo:
        if betu in maganhangzok:
            osszesen += 1
    return osszesen

print(mhszamol("Aladár"))

print("---")

def helyettesit(szo, alt):
    return szo.replace('a', alt)

print(helyettesit("Bruh", alt="u"))

print("---")

from random import randint
veletenszam = randint(1, 10)
probakszama = 3

while probakszama > 0:
    tipp = int(input("Tippelj: "))
    if tipp == veletenszam:
        print("Nyertél!")
        break
    else:
        probakszama -= 1
        print("Hibás tipp!")
else:
    print("Vesztettél!")


print("---")

def listaosszeg(lista):
    osszeg = 0
    for elem in lista:
        if isinstance(elem, list):
            osszeg += listaosszeg(elem)
        else:
            osszeg += elem
    return osszeg

print(listaosszeg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print("---")

def felez(szam1, szam2):
    szamlalo = 0
    while szam1 > szam2:
        szam1 /= 2
        szamlalo += 1
    return szamlalo

print(felez(1,2))

print("---")

def median(lista):
    rendezett = sorted(lista)
    if len(rendezett) % 2 == 1:
        return rendezett[len(rendezett) // 2]
    else:
        kozepso1 = rendezett[len(rendezett) // 2 - 1]
        kozepso2 = rendezett[len(rendezett) // 2]
        return (kozepso1 + kozepso2) / 2

print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print("---")
