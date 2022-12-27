"""Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
"""

def mediumValue(list):
    soma = 0
    for element in list:
        soma += element
    media = soma/(len(list))
    return media    
        
# amostra aleatoriamente 50 números do intervalo 0...500

import random
random_list = random.sample(range(500), 50)

random_list.sort()

print(random_list)

length = len(random_list)

print('Menor:', random_list[0])

print('Maior:', random_list[length-1])

print('Média',mediumValue(random_list))

print('Mediana:', random_list[int(length/2)])

