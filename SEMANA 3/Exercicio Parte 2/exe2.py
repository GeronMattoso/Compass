"""Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Faça um programa que gere uma nova lista contendo apenas números ímpares."""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []

for element in a:
        if element%2 != 0:
            b.append(element)
        else:
            pass
print(b)