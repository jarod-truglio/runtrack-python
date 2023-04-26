# Définition de la fonction password, création de la variable mdp, il parcour mdp et si celui ci à moins de 8 caractère alors il retourne que c'est
# Faux, création des varaible l,m,n,s , dans la bibliotèque je parcours la variable mdp, si dans mdp il y à des minuscule de a à z, retourne l =
# vrai, si dans mdp il y à des majuscule(.isupper()) alors retourne m = vrai, si dans mdp  il y à un chiffre entre 0 et 9, retourne n = vrai
# si dans mdp il y a un caractère spéciale alors s = vrai, retourner l et m et n et s, demandez à l'utilisateur d'écrire un mot de pass, si le mot
# le mot de passe est faux alors écrire Erreur de saisie du mot de passe et demandez de choisir un autre mot passe, si vrai écrire Mot de passe 
# actualisé !, après avoir importé haslib et avoir écrit un mot de passe valide, créer une varaible encodage qui va encodé la variable mdp
# (hashlib.sha256(mdp.encode())), puis écrire Le mot de passe crypté est :, et écrire le mdp encodé (encodage.hexdigest()).

def password(mdp):
    if len(mdp) < 8:
        return False
    l = False
    m = False
    n = False
    s = False
    for i in range(len(mdp)):
        if mdp[i] >= "a" and mdp[i] <= "z":
            l = True
        if mdp[i].isupper():
            m = True
        if mdp[i] >= "0" and mdp[i] <= "9":
            n = True
        if mdp[i] in "!@#$%^&*":
            s = True
    return l and m and n and s

import hashlib

mdp = input('Choisissez un mot de passe : ')
while password(mdp) == False:
    print("Erreur de saisie du mot de passe ")
    mdp = input("veuillez choisir un autre mot passe : ")
print("Mot de passe actualisé !")

encodage = hashlib.sha256(mdp.encode())
print("Le mot de passe crypté est :", encodage.hexdigest())