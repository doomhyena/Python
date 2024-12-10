'''
import random

lista = []


# töltse fel a listát 20 darab véletlen gemerált számmal 1 és 100 között

for i in range(20):
    lista.append(random.randint(1, 100))

print("Lista: ", lista)

for n in lista:
    print(n)

szam = 0
while (szam > 10 and szam % 2 == 0):
    print(szam)
    szam += 1
else:
    print("A while ciklus vege")
'''

a = 0

def met1():
    a = 10
    print(f"a: {a}")

met1()
print(f"a: {a}")
