# Dans la Liste "L" si i(le chiffre) divisé par 3 = à O alors rajoutez +1 à M, puis écrire M pour compter le nombre de multiples

L = [8, 24, 48, 2, 16]
M = 0
for i in L:
    if i % 3 == 0:
        M += 1

print(M)