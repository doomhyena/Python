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

#print(kozos('Háló', 'Faház'))

#----------------------------------------------------------------------------------------------------------------

def kozos2(szo1, szo2):
    return ''.join(sorted(set(szo1.lower()) & set(szo2.lower())))
#print(kozos2('Háló', 'Faház'))

#----------------------------------------------------------------------------------------------------------------

'''

A metódus szűrje ki csak az igaz egyeneleteket
Pl.: (['1+1=2', '2+2=3', '3+3=6']) --> ['1+1=2', '3+3=6']

'''

def egyenlet(egyenletlista):
    igazegyenletek = []
    for i in egyenletlista:
        a, b = i.split('=')
        if eval(a) == int(b):
            igazegyenletek.append(i)
    return igazegyenletek

#print(egyenlet(['1+1=2', '2+2=3', '3+3=6']))

#----------------------------------------------------------------------------------------------------------------

"""

Logikai tagadás: if not

Tartalom ellenőrzése

karakter = 'a'

szoveg = 'abcde'

if karakter in szoveg:
    return True
"""

'''

A metódus visszaadja, hogy átlagosan hány betűből állnak a mondat szavai

Pl.: atlagszohossz("Ez egy példa mondat") -->  4.00
    - A megoldást 2 tizedesjegyre kerekítjük
    - Csak a rendes betűk számítanak. A spec karakterek(,:?!-,) nem.
    - Használjuk: a for, in, round(), not, count(), if

'''

def atlaghossz(mondat):
    spec_karakterek = ',,:?!-,()'

    szavak = mondat.split()

    szohossz = []

    for szo in szavak:
        hossz = 0
        for karakter in szo:
            if not karakter in spec_karakterek:
                hossz += 1
        if hossz > 0:
            szohossz.append(hossz)

        atlag = round(sum(szohossz) / len(szohossz), 2)

        return atlag

print(atlaghossz("Ez egy példa mondat, mert megtehetem."))
