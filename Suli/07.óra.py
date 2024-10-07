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

#----------------------------------------------------------------------------------------------------------------

def kozos2(szo1, szo2):
    return ''.join(sorted(set(szo1.lower()) & set(szo2.lower())))
print(kozos2('Háló', 'Faház'))

#----------------------------------------------------------------------------------------------------------------

'''

A metódus szűrje ki csak az igaz egyeneleteket
Pl.: (['1+1=2', '2+2=3', '3+3=6']) --> ['1+1=2', '3+3=6']

'''


