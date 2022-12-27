"""Peça para o usuário digitar uma palavra pelo teclado e determina se a palavra digitada é ou não um
palíndromo. Um palíndromo é uma palavra que permanece igual se lida de traz pra frente.
"""

def inverter(palavra:str):
    return palavra[::-1]


palavra = input("digite uma palavra")
palavraInv = inverter(palavra)

if palavra == palavraInv:
    print("A palavra {} é um palindromo seu inverso é {}".format(palavra, palavraInv))
else:
    print("A palavra {} NÃO é um palindromo seu inverso é {}".format(palavra, palavraInv))