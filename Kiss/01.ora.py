#programiz.com (Python)
i = 5 #i nevű változó, mögöttes érték: 5
j = "alma" #szöveges változó
#Nem kell megadni a típust, magától értelmezi
#Egysoros komment
'''többsoros 
komment'''
k = 7
l = i + k #változón belüli összeadás
print(l) #kiíratás
#k mindkét esetben nő 1-gyel:
k = k+1
k += 1
#----------------------------------------------
#Függvények/metódusok:
'''def metódusnév(paraméterek):
    A metódus kódja
    return művelet'''

#print(metódusnév(konkrétÉrték))
#Konkrét példa (faktoriális számítása):
#Faktoriális: 4! = 4*3*2*1 = 24
def faktorialis(szam):
    megoldas = 1 #ebben lesz a végeredmény
    for i in range(szam): #a ciklus 1-től "szám"-ig megy
        megoldas *= i+1 #minden körben szoroz
    return megoldas #a végén visszakérem az eredményt

'''for ciklus:
    - újra és újra elvégez egy adott műveletet
    - i: egy segédváltozó (minden körben növekszik)
    - range(): az, hogy meddig menjen
    - tartalom: az, amit a ciklus minden krben elvégez
'''
print(faktorialis(4))
#-------------------
'''Feltételes műveletek (if-else):
    - if = "Ha"
    - else = "Másik"
Séma:
if LogikaiFeltétel:
    Lefutó kód, ha teljesül
else:
    Minden más esetben ez a kód fut le
'''
#Külön eset 0-ra: 0! = 1
def faktorialis2(szam):
    megoldas = 1
    #0 esetén egy külön művelettel oldja meg:
    if szam == 0:
        return megoldas
    #Minden egyéb esetben a megszokott művelet kell:
    else:
        for i in range(szam):
            megoldas *= i+1
    return megoldas
#Szimpla egyenlőségjel (=): deklaráció, kijelentés
#Dupla egyenlőségjel (==): összehasonlítás
print(faktorialis2(4))
print(faktorialis2(0)) #újrafelhasználás
#--------------------------
'''Listák/Tömbök:
    - összetett objektumok, melyek al-elemeket tartalmaznak
    - minden al-elemnek van egy sorszáma
    - [] zárójellel jelöljük
'''
lista1 = [4,5,1,3] #lista1 nevű számlista
#szedjük ki az első számot egy külön változóba:
elem1 = lista1[0] #0. index = 1. elem
'''
Listaindex:
    - a listaelem sorszáma
    - 0-val kezdődik az indexelés
    - formája: listanév[index]
'''
print(elem1)
#---------------
#Feladat: egy metódus találja meg és írja egy lista legnagyobb számát.
def legnagyobb(lista):
    maximum = lista[0] #Kezdetben úgyis az 1. szám a legnagyobb
    #Menjen végig a lista számain:
    for i in lista:
    #Ha az adott szám nagyobb, mint az eddigi max:
        if i > maximum:
            #Akkor az lesz az új max:
            maximum = i
    return maximum #Végül visszakérjük

print(legnagyobb([2,5,1]))
#Feladat: a legkisebb számot találja meg.
#------------------------------------
#Minimum és maximum meghatározása beépített parancsokkal:
def minmax(lista):
    lk = min(lista) #legkisebb szám
    ln = max(lista) #legnagyobb szám
    return lk, ln
print(minmax([2,5,1]))
#------------------------------------
#Hány magánhangzó van egy bekért szóban?
def mhszámol(szo):
    maganhangzok = ['a','e','i','o','u'] #ezeket számoljuk meg
    osszesen = 0 #talált magánhangzók száma lesz
    for i in szo: #végigmegyünk a szó betűin
        if i in maganhangzok: #"ha a betű szerepel a listában..."
            osszesen += 1 #"...akkor a megoldás növekedjen."
    return osszesen

print(mhszámol("alma"))
#---------
def mhszámol2(szo):
    mh = "aeiou" #Lista helyett 1 db string szöveg
    összesen = 0
    for i in szo:
        if i in mh:
            összesen = összesen + 1 #alternaív hozzáadás
    return összesen
#--------
#Feladat: a bekért szóban helyettesítsük a magánhangzókat egy tetszőleges karakterrel.
#print(helyettesit("alma","*")) --> "*lm*"
def helyettesit(szo,alt):
    maghangz = ['a','e','i','o','u'] #cserélendő betűk
    megoldas = szo #kezdetben az eredeti szó a mo.
    for i in szo: #végigmegy a szó betűin
        if i in maghangz: #ha az adott betű szerepel a listában
            megoldas = megoldas.replace(i,alt) #akkor azt a betűt kicseréljük a felhasználó által megadott cenzúrakarakterre.
#replace(Mit,Mire): kicserél egy adott betűt a szóban, egy másik adott karakterre
    return megoldas
#-----------------------
'''Nagybetű ellenőrzése: Betű.isupper() --> igaz/hamis értéket ad
Listához fűzés: Listanév.append(ÚjElem)
Feladat: Keressük meg egy szövegben a nagybetűk indexét (sorszám).'''

def indexkeres(szo):
    megoldas = [] #ebbe kerülnek majd a sorszámok (indexek)
    for betu in szo: #a for végigmegy a szó betűin
        if betu.isupper(): #"Ha az adott betű az nagybetű..."
#"...akkor adja hozzá a sorszámát a megoldáslistához."
            megoldas.append(szo.index(betu))
#szo.index(betu): a szónak azon sorszáma (indexe), aminél a talált betű van
    return megoldas
#---Alternatív megoldás:
def indexkeres2(szo):
    megoldas = []
    for i in range(len(szo)):#annyi kört megy, ahány betű van
        if (i.isupper()):
            megoldas.append(i)
    return megoldas
'''
len(változó): változó elemeinek a száma (length = hossz)
isupper(): nagybetű-e
append(): lista végéhez fűzés
'''
#--------------------------------------
'''While ciklus: addig fut, ameddig még teljesül a benne 
    megfogalmazott logikai feltétel.
Feladat: a metódus 2 számot kér be. Addig felezi az elsőt, amég
    az nem csökken a mások szám alá. MO: hányszor kellett megfelezni.
Pl.: print(felez(4666,544)) --> 3 (mert: 4666, 2333, 1166, 583)'''
def felez(szam1,szam2):
    szamol = 0 #felezések számát fogja tárolni
    while szam1 > szam2: #While = "ameddig"
        szam1 = szam1 / 2 #megfelezi szam1 értékét
        szamol += 1 #feljegyzi, hogy történt egy felezés
#Egy idő után szam1 kisebb lesz, mint szam2. Ekkortól nem teljesük a while ciklusba foglalt feltétel és megtörik a ciklus.
    return szamol-1
#--------------------------------------------------
'''A felhasználónak 3 lehetősége van eltalálni egy random 1-10 közötti számot.
A konzolon keresztül adja meg a tippjeit.'''
#Beimportáljuk a random modul randint szegmensét:
from random import randint
#Generáljon egy 1-10 közti véletlenszerű egész számot:
véletenszám = randint(1,10) #randint = "random integer"
#3 próba van, ha azokból nem találja ki, akkor veszít.
#Számon tartjuk a hátralévő tippek számát:
próbákSzáma = 3
#addig megy a játék, ameddig el nem fogy a próba:
while próbákSzáma > 0:
#A konzol bekér egy számot, amit elrakunk a tipp változóba:
    tipp = int(input("Tippelj:"))
    if (tipp == véletenszám): #Ha a tipp talált
        print("Nyertél!") #akkor megjelenik a "Nyertél" üzenet
        break #és idő előtt megtörik a while ciklus
    else: #egyéb esetben, tehát ha nem találtuk el
        próbákSzáma -= 1 #akkor csökken a hátralévő próbák száma
        print("Hibás tipp!") #és jelezzük is
else: #ez az else a while ciklushoz tartozik (próbákSzáma = lett 0-val)
    print("Vesztettél!") #akkor vesztettünk.
#-------------------------------------------
"""

Összetett tömbök: [2,[3,4],5] (tehát van benne allista)
Ennek ellenére összegezzük a teljes tartalmat:

"""
def listaösszeg(lista):
    megoldas = 0
    for i in lista:
        if type(i) == int: #ha az adot elem típusa "int/szám..."
            megoldas = megoldas + i #akkor csak simán házzáadja
        else: #ez akkor fut le, ha al-listát talál
            megoldas = megoldas + listaösszeg(i) #meghívja önmagát az allistára
    return megoldas

print(listaösszeg([2,[3,4],5]))
#---------------------------------------
'''Feladat: Hány al-lista van a nagylistában?
Pl.: print(alszám([[2,1],3,5,[7,6]])) --> 2'''
def alszám(nagylista):
    megoldás = 0 #talált al-listák száma lesz
    for i in nagylista:
        if type(i) == list: #Ha az adott elem 'list' típusú, akkor az egy allista
            megoldás += 1
    return megoldás
#---Alternatív megoldás:
def alszám2(nagylista):
    return str(nagylista).count('[')-1
#str(változó): string szövegként értelmezi a tartalmát
#count('karakter'): megszámolja, hogy hány darab van az adott karakterből
#Csak az al-listákat kellett megszámolni, így a főlista miatt -1 az eredményből