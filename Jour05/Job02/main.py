# La Fonction draw_rectangle prend 2 variable width et height, si i dans la variable height est = à 0 ou -1 alors écrire "-" * width (10 *),
# sinon écrire | + espace * width -2 + | ( -2 car sinon il ferais 10 espace au lieu de 8 pour faire un rectangle).

def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('-' * width)
        else:
            print('|' + ' ' * (width - 2) + '|')

draw_rectangle(10, 3)