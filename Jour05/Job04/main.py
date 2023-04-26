def chiffrement_cesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_chiffre = ''
    for lettre in message:
        if lettre.lower() in alphabet:
            indice_lettre = alphabet.index(lettre.lower())
            nouvel_indice = (indice_lettre + decalage) % 26
            if lettre.isupper():
                message_chiffre += alphabet[nouvel_indice].upper()
            else:
                message_chiffre += alphabet[nouvel_indice]
        else:
            message_chiffre += lettre
    return message_chiffre

message = "Bonjour tout le monde !"
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)
print(message_chiffre)