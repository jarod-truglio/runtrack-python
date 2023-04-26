def Marchand(type,saison):
    if type == "fruit" and saison == "hiver":
        return "orange, mandarine et kiwi"
    elif type == "fruit" and saison == "ete":
        return "Poire, fraise, cassis"
    elif type == "legume" and saison == "hiver":
        return "carotte, topinambour, endive"
    elif type == "legume" and saison == "ete":
        return "artichaut, aubergine,navet"
    else :
        return "Erreur de saisie"
    
print(Marchand("fruit","hiver"))