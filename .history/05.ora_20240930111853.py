def halmazok(halmazok, szam):
    szamol = 0
    for i in halmazok:
        if i[1] == szam or i[1] == szam:
            szamol += 1
        else:
            for j in range(i[0], i[1]):
                if j == szam:
                    szamol += 1
    return szamol

# ---------------------------------------------------------------------------------------------                

def matrixos(sor, oszlop, *karakter):
    if karakter:
        return [''.join(karakter*oszlop) for _ in range(sor)]
    else:
        return ['#'*oszlop for _ in range(sor)]
    
# ---------------------------------------------------------------------------------------------                

def egyeznek(szampar):
    num1 = str(szampar[0])
    num2 = str(szampar[1]) 
    jegyek1 = 0
    jegyek2 = 0

    for i in num1:
        jegyek1 = int(num1[i])
    for i in num2:
        jegyek2 =int(num2[i])

    return jegyek1 == jegyek2

# ---------------------------------------------------------------------------------------------                

def darabszam(n):
    megoldas = []
    for i in range(n):
        alttomb = []
        for j in range(n):
            alttomb.append(n)
        megoldas.append(alttomb)
    return megoldas        

# ---------------------------------------------------------------------------------------------                

def darabszam2(n):
    return [[n] * n] * n

def vizsgal(egyenlőtlenseg):
    lista = [int(i) if i.isdigit() else i for i in egyenlőtlenseg.split()]

    for i in range(0, len(lista)-2, 2):
        if lista[i + 4] == '>':
            if lista[i] <= lista[i+2]:
                return False
            elif lista[i + 1] == '<':
                if lista[i] >= lista [i + 2]:
                    return False
        return True        
    
# ---------------------------------------------------------------------------------------------                

def elofordulas(start, veg, ertek):
    intervallum = range(start, veg + 1)
    szamol = 0
    for i in intervallum:
        szovegkent = str(abs(i))
        if szovegkent in intervallum :
            szamol += 1
        continue
    return szamol    

# ---------------------------------------------------------------------------------------------                

lista1 = ()
lista2 = ()

egyformak = set(lista1) == set(lista2)
