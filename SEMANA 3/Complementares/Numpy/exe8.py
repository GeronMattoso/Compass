import numpy as np

array = np.arange(25).reshape(5, 5)

meanLines = np.mean(array[[0,2,3][:]], axis=1)
meanColunms = np.mean(array[:][:,[0,1,4]], axis=0)
diagSum = array.trace() + np.fliplr(array).trace()

print(array)

print("Média linhas 0, 2 e 3:", meanLines)
print("Média colunas 0, 1 e 4:", meanColunms)
print("A soma das duas diagonais:", diagSum)