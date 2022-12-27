import numpy as np

def diagSum(array):
    soma = 0
    for lin in range(array.shape[0]):
        for col in range(array.shape[1]):
            if lin==col:
                soma += array[lin][col]
    return soma

array = np.arange(1,26)
array = array.reshape((5,5))

soma = diagSum(array)

print(array)
print(soma)

#print(np.trace(array))