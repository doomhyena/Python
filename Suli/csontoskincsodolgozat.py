'''

1. feladat:
A metódus egy darab számot vizsgáljon.
A kérdés, hogy az alábbi állítás igaz-e: (2**SZÁM+1) maradék nélkül osztható (2 * SZÁM + 1)-gyel?
Pl.: print(osztható(5)) --> Eredmény: True   
mert: 	2**5+1 = 33
	2*5+1  = 11
	33 / 11 = 3 egész
	Tehát 5 esetén True

Tippek: if-else, % osztás, egyenlőségjelek száma a logikai vizsgálatnál.
#----------
2. feladat:
A metódus vegyen be egy intervallumot és egy osztót.
Az intervallumon belül mely számok oszthatók az osztóval?
Pl.: print(osztótkeresés(1, 10, 3)) --> Eredmény: [3, 6, 9]
mert:	1 és 10 között a 3, 6 és 9 oszthatók 3-mal.

Tippek: kezdetben üres tömb a megoldásnak, for ciklus (tól,ig), append(), 
	if, % osztás, egyenlőségjelek száma a logikai vizsgálatnál.
#----------


'''
def osztható(szám):
    kifejezes1 = 2 ** szám + 1
    kifejezes2 = 2 * szám + 1
    
    if kifejezes1 % kifejezes2 == 0:
        return True
    else:
        return False

print(osztható(5))

# -------------------
def osztótkeresés(tól, ig, osztó):
    eredmeny = []
    
    for szám in range(tól, ig + 1): 
        if szám % osztó == 0:
            eredmeny.append(szám)  
            
    return eredmeny

print(osztótkeresés(1, 10, 3))
