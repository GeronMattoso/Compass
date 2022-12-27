import numpy as np

def arrayProd(a, b):
    try:
        return a.dot(b)
    except:
        print("Não é possivel realizar o produto entre essas duas matrizes")
        exit()

a = np.random.uniform(size=(5,3))
b = np.random.uniform(size=(3,4))

print(arrayProd(a,b))
