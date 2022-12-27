"""Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
Dica: leia documentação da função open(...), link: https://docs.python.org/3/library/functions.html#open"""

with open("texto.txt", "r") as arquivo:
    print(arquivo.read())