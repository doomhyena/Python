def halmazok(halmazok, szam):
    szamol =0
    for i in halmazok:
        if i[1] == szam or i[1] == szam:
            szamol += 1
        else:
            for j in range(i[0], i[1]):
                if j == szam:
                    szamol += 1
    return szamol

# ---------------------------------------------------------------------------------------------                
