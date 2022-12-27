import numpy as np

def maxToZero(array):
    max = array.max()
    print("\nValor maximo era:", max)
    array[array >= max] = 0
    return array

array2D = np.random.normal(0, 3, size=(5, 5))

#print(array2D)

print(maxToZero(array2D))