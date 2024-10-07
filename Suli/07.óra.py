"""

A metódus 2 szót vizsgál és visszadja a közös betüket.
Pl.: közös("háló", "faház") --> há

"""

def kozos(szo1, szo2):
    kozosek = []
    for i in szo1.lower():
        if i in szo2.lower():
            kozosek.append(i)
    return ''.join(sorted(set(kozosek)))

print(kozos('Háló', 'Faház'))