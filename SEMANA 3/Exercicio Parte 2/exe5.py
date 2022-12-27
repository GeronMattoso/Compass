"""Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize um
exemplo para testar sua função."""

def noDup (lista):
    return list(set(lista))

##samples
a = [1, 1, 2, 3, 5, 5, 8, 13, 21, 34, 55, 89, 89]
b = [5,5,6,6,6,6,6,6,7,7,7,4,4]

print(noDup(a))
print(noDup(b))