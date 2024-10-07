def mondatos(mondat):
    valasz = ''
    for betu in mondat:
        if betu.isupper():
            valasz += ' ' + betu.lower()
        else:
            valasz += betu
    return valasz

#print(mondatos("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur et ante lorem. Aenean consequat egestas nisl, id facilisis nunc placerat eget. Proin nec congue sem"))

#----------------------------------------------------------------------------------------------------------------

szo = 'alma'
szo = szo.replace('a', 'x')

#print(szo)

"""

Feladat: Ez egy példa mondat --> Ez egy ***** ******

"""

def cenzura(mondat):
    for szo in mondat.split():
        if len(szo) > 4:
            mondat = mondat.replace(szo, "*" * len(szo))
        return mondat

#print(cenzura('Ez egy példa mondat, consectetur'))

#----------------------------------------------------------------------------------------------------------------

def cenzura2(mondat):
    szavak = mondat.split()
    for i in range(len(szavak)):
        if len(szavak[i] > 4):
            szavak[i] = "*" * len(szavak[i])
    return " ".join(szavak)

#print(cenzura('Ez egy példa mondat, consectetur'))

#----------------------------------------------------------------------------------------------------------------

ertek = 4
ertek2 = 5
szoveg = "A tárolt tartalom az {} és {}".format(ertek, ertek2)
szoveg2 = f"A tárolt tartalom az {ertek} és {ertek2}"

print(szoveg)
print(szoveg2)

lista1 = 'abcd'
lista2 = lista1[2:]

print(lista2)

#----------------------------------------------------------------------------------------------------------------

def penzes(regi, uj):
    regi = int(regi[1:])
    uj = int(regi[1:])
    szazalek = int(100*uj/regi-100)
    return '{}%-os,'.format(abs(szazalek), 'növekedés' if szazalek > 0 else 'csökkenés')

print(penzes('$400','É700'))