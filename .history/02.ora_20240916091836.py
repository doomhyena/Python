import statistics

def median(lista):
    hossz = len(lista)
    rendezett = sorted(lista)
    if (hossz % 2 == 1):
        return rendezett(hossz//2)
    else:
         x1 = rendezett[hossz//2]
         x2 = rendezett(hossz//2+1)
         x3 = (x1 + x2)/2

         return round(x3, 1)

def median(lista):
    return statistics.median(lista)
 
 # --------------------------------------------------------
 
def jegykulonbseg(num1, num2): 
    osszeg = 0
    szam1 = str(num1)
    szam2 = str(num2)

    for i in range(len(szam1)): 
        osszeg += abs(int(szam1[1]) - int(szam2[1]))
    return osszeg

def akkumlator(lista):
    if len(lista) == 0:
        return []
    else:
        megoldas = []
        osszeg = 0
        for i in lista:
            osszeg += 1
            megoldas.append(lista)
akkumlator(5, 5, 1, 2)