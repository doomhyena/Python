def median(lista):
    hossz = len(lista)
    rendezett = sorted(lista)
    if (hossz % 2 == 1):
        return rendezett(hossz)