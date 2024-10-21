
"""
Van egy intervallum, amin belül meg akarjuk keresni a legnagyobb prímszámot. 
A metódus 2 bevott számot vizsgál: az intervallum kezdetét és végét. 
Pl.: legnagyobbprím(2, 10) --> 7 (2, és 10 között 7 a legnagyobb prím) 
Ha fordítva adjuk meg a határértékelet pl.: (10, 2) akkor is működjönn. 
Tippek: if, for belső for a másikba, % int(), range()

"""

def legnagyobbprím(a,b):
    if a > b:
        c = a
        a = b
        b = c
    
    for i in range(b, a-1, -1):
            osztokszama = 0
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    osztokszama += 1
            if osztokszama == 0:
                 return i

print(legnagyobbprím(2, 10)) 
print(legnagyobbprím(10, 2))  




"""

def legnagyobbprím(a, b):
    if a > b:
        a, b = b, a
        for i in range(a, b):
            if i > 1:
                príme = True
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                    else:
                        legnagyobb = i       
        return legnagyobb
                        
print(legnagyobbprím(1, 10))
print(legnagyobbprím(10, 1))                   


"""
