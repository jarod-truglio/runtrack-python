# J'écrit la liste "L", puis je parcour(len) la liste "L"(lent(L)), puis j'ajoute à chaque i(le nombre) de la liste +1, puis j'écrit le résultat

L = [7, 11, 42, 39, 2]
print("La liste initiale est :", L)
for i in range(len(L)):
    L[i] += 1
print("La liste modifiée est :", L)