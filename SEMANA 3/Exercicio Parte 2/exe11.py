"""Escreva um programa que leia do teclado uma sequência de número separados por vírgula (e.g. 2,4,5,6,1,6) e
imprime a soma de todos eles."""


def sum (lista):
    total = 0
    numeros = []

    for element in lista:
        if element != ',':
            numeros.append(element)
        else:
            pass
    
    for element in numeros:
        total += int(element)
    return total


list = input("Numeros:")

print('Soma:',sum(list))

