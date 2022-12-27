"""
Dada as listas a seguir:
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
Faça um programa que imprima os dados na seguinte estrutura: " - está com anos"
"""

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

zipList = list(zip(primeirosNomes, sobreNomes, idades))


for element in zipList:
    print("{} {} está com {} anos" .format(element[0], element[1], element[2]))