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
        else:
            ismetlodok.append(i)
    if (len(ismetlodok) > 0):
        rendezett = sorted(ismetlodok)
    return None
    
def xosszeg(lista, x):
    sorszam = 1
    osszeg = 0  
    for i in lista:
        if sorszam == x:    
            osszeg = osszeg + x
            sorszam = 0
            sorszam = sorszam + 1
        return osszeg

def ossezg(szam):
    if szam % 2 == 1:
        return True
    else:
        return False

# ---------------------     