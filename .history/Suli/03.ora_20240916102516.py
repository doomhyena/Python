def dobasok(lista):
    pontszam = 0
    for a, b in lista:
        if a == b:
            return 0
        pontszam += a + b