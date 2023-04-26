# Quand i( le chiffre de la list "L") est inférieur à MN alors remplacer MN par se chiffre, et quand i est plus grand que MX 
# alors remplacer MX par ce chiffre, puis écrire MN et MX
# !!! MN et MX on pour base le premier chiffre de L (MN = L[0] et MX = L[0]) c'est à dire 8

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
MN = L[0]
MX = L[0]
for i in L:
    if i < MN:
        MN = i
    if i > MX:
        MX = i
print("Le minimum de la liste est : ", MN)
print("Le maximum de la liste est : ", MX)