"""Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como
segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida retorna o
resultado em uma nova lista.
Teste sua função para saber se está ok"""

def soma1(valor):
    return valor + 1

def quadrado(valor):
    return valor*valor

def Upper(frase):
    return frase.upper()

def my_map(list, f):
    result = []
    for element in list:
        result.append(f(element))   
    return result

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b = ["arroz","feijao","batata"]


print(my_map(a, soma1))

print(my_map(a, quadrado))

print(my_map(b, Upper))