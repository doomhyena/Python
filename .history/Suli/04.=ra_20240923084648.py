"""

while ciklus:
    Egymáss után többször rlvégez egy művletet (mint a for)
    Addig fut a ciklus amíg újra és újra teljesül a benne megfogalmazott logikai feltétel (mit egy ifben)
"""

# Addig gyűjtünk minden nap félre rerakunk rá egy összeget, de van egy kezdőérték is.

"""

Pl.: 1 2 3 4 5 6 7
    2 3 4 5 6 7 8 (amíg el nem érjüo az árat)

"""


def sporol(ar, toke, kezd):
    osszeg, napok = 0, 0
    ar -= toke


    while osszeg < ar:
        i = kezd + napok/7 if not