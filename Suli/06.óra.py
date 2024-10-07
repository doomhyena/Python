def mondatos(mondat):
    valasz = ''
    for betu in mondat:
        if betu.isupper():
            valasz += ' ' + betu.lower()
        else:
            valasz += betu
    return valasz

#print(mondatos("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur et ante lorem. Aenean consequat egestas nisl, id facilisis nunc placerat eget. Proin nec congue sem"))

#-------------------------------------------------

szo = 'alma'
szo = szo.replace('a', 'x')

#print(szo)

"""

Feladat: Ez egy példa mondat --> Ez egy ***** ******

"""

def cenzura(mondat):
    for szo in mondat.split():
        if len(szo) > 4:
            mondat = mondat.replace(szo, "*"*len(szo))
        return mondat

#print(cenzura('Ez egy példa mondat'))