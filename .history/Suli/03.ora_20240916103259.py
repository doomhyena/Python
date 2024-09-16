def dobasok(lista):
    pontszam = 0
    for a, b in lista:
        if a == b:
            return 0
        pontszam += a + b
    return pontszam    

def ismetlodok(lista):
    egyediek = []
    ismetlodok = []
    for i in lista:
        if i not in egyediek:
            egyediek.append(i)