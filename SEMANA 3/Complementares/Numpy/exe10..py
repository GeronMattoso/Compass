import numpy as np

array = np.random.randint(0, 50, (5, 5))

#print(array)

ordenado = list(set(np.sort(array, axis = None)))#lista com valores ordenados e sem repticao
print("removidos:", ordenado[0:][:5])
print("------------------")

print(array)
print("------------------")
array[array <= ordenado[4]] = -1 # remove todos valores menores ou iguais ao quinto da lista dos ordenados
print(array)
