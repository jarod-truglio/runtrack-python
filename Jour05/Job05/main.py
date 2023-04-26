# Création de la fonction Toilette, quand utilisé alors convertire la la hauteur en metre en la divisant par 100, puis calcule la
# distance par jour à hauteur de 5 * 2 (5* la hauteur d'une marche * 2 pour aller retour * les mètres), multiplie par 7
# Pour obtenir la distance par semaine, et donc la distance total avec distance semaine * mètre puis retourner les informations

def Toilette(M, H):
    HM = H / 100 
    DJ = 5 * 2 * HM 
    DS = DJ * 7 
    DT = DS * M
    return f"Pour {M} marches de {H} cm, le gardien parcours {DT:.2f} m par semaine."

print(Toilette(100, 20))