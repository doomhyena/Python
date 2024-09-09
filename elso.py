i = 5
k = 7
k= k + i
print(i + k)

# Függvény
"""
def függvénynév(paraméterek)_
    A kód
    return elmélet

print(függvénynév(oaraméterek))    

"""

def faktoriális(szam):
    megoldas = 1
    for i in range(1, szam + 1):
        megoldas *= i
    return megoldas

print(faktoriális(5))

def kuki(szam):
    if szam == 0:
        return 1
    else:
        megoldas = 1
        for i in range(1, szam + 1):
            megoldas *= i
        return megoldas

print(kuki(0))


listal = [1, 2, 3, 4, 5]

elsoelem = listal[0]

print(elsoelem)
print(listal[0])


def legnagyobb(lista):
    maximum = lista[0]
    for i in lista:
        if i > maximum:
            maximum = 1
        return maximum

print(legnagyobb([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))

def minimax(lista):
    a = min(lista)  
    b = max(lista) 
    return a, b

print(minimax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))


def ehe(valtoz):
    massalhangzok = ["b", "c", "d", "g", "gy"]
    osszesen = 0
    for i in szo:
        if i in massalhangzok:
            osszesen =+ 1
    return osszesen

print(ehe("bruh"))    

def helyetessites(szo, karakter):
    mghnzk = ["a", "e", "i", "o", "u"]
    megoldas = szo
    for i in szo:
        if i in mghnzk:
            megoldas = megoldas.replace(i.replace(karakter))
        return megoldas

# print()

def indexkeres(szo):
    megoldas = []
    for i in szo:
        if i.upper():
            megoldas.append(szo.index(i))
        return megoldas    

def indexkers(szo):
    megoldas = []    
    for i in range(len(szo)):
        if (str.isupper(szo[i])):
            megoldas.append(i)
    return megoldas        

def fekez(szam1, szam2):
    szam1 = 0
    while szam1 > szam2:
        szam1 = szam1 / 2
        szam1 =+1
    return szam1 - 1

from random import random

whileszam = random(1, 10)
próbaszam = 3

while próbaszam > 0:
    tipp = int(input("Tippelj egy számot! Három lehetőséged van!: "))

    if (tipp == whileszam):
        print("Gratulálok, eltaláltad a számot!")
    else:
        print("Hibás tipp!")    
else:
    print(f"Vesztettél! A számod ez volt!: " + whileszam) 

def listaosszeg(lista):           
    megoldas = 0
    for i in lista:
        if type(i) == int:
            megoldas = megoldas + i
        else:
            megoldas = megoldas + listaosszeg(i)
    return megoldas

print(listaosszeg(2,[1, 2,], 4))


def alszam(nagylista):
    megoldas = 0
    for i in nagylista:
        if type(i) == list:
            megoldas += 1
    return megoldas

def aszlam2(nagylista):
    return str(nagylista).count('[') - 1