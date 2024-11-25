a = 7
b = 9

print(a)
print(b)

a = "auto"
b = 7

print(a, b)

c = int(17)
print(c)
c = float(17)
print(c)
c = str(17)
print(c)
c = bool(17)
print(c)

c = True

print(type(c))

d = "auto"
D = "auto"

print(d, D)

e,f,g,h = "auto", "auto", "auto", "auto"

import random as rnd

z = rnd.randint(1, 100)

print("1 és 100 közötti szám:", z)
"""
y = min(z, b, h)
x = max(z, b, h, a, c)

print(y)
print(x)
"""

w = abs(-15)
v = pow(5, 2)

print(w)
print(v)

import math as m

u = m.sqrt(500)

print(u)

t = m.pi

print(t)

A = 7
B = 9

if A > B:
    print("A nagyobb")
elif A < B:
    print("B nagyobb")
else:
    print("A két szmám egyenlő")

# input

sajat = input("Adj meg egy számot: ")
sajat = int(sajat)
print("A szám:", sajat) # for, while, metódusok
