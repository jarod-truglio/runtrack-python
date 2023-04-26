L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
S = 0
for i in L:
    if i > 25:
        S += i
    if i > 90:
        break
    
print(S)