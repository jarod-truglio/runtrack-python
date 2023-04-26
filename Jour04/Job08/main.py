# Dans la Liste "L" si i(le chiffre) divisé par 2(pour savoir si ils sont pairs on divise par 2) = à O alors i(le chiffre en question) est 
# additionné à S, puis écrire S pour savoir combien vaut les chiffres paires additionnés

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
S = 0
for i in L:
    if i % 2 == 0:
        S += i
print(S)