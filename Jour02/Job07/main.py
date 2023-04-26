def Text(langage):
    if langage == "javascript":
        return "Tu est développeur WEB"
    elif langage == "python":
        return "tu es un developpeur IA"
    elif langage == "java":
        return "Tu est developpeur logiciel"
    elif langage == "reactjs":
        return "Tu est developpeur mobile"
    else :
        return "un jour, je serai le meilleur developpeur... "

print(Text("javascript"))