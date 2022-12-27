import numpy as np

def SumLines(array):
    return np.sum(array, axis = 1)

def SumColumns(array):
    return np.sum(array, axis = 0)

def lastLineMean(array):
    return np.mean(array, axis=1)[-1]

def lastColumnMean(array):
    return np.mean(array, axis=0)[-1]

array = np.arange(2,51,2)
array = array.reshape((5,5))

print(array)

print("Soma da linhas", SumLines(array))

print("Soma da colunas", SumColumns(array))

print ("Média da última linha =", lastLineMean(array))

print("Média da última Column =", lastColumnMean(array))