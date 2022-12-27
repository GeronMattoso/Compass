import numpy as np

array = np.arange(25).reshape(5, 5)
print(array)
print("\n")

pares = np.where(array%2==0)
print("Pares:", array[pares])

maior8 = np.where(array>8)
print("Maiores que 8:", array[maior8])