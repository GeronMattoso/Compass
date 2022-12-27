import numpy as np

a = np.array([[0,3,4,5], [7, 10, 9, 2]])
b = np.array([[1,4,9,12], [15, 22, 19, 17]])

print(a)
print("\n")
print(b)
print("\n")

c = np.concatenate((a,b), axis = 0)
print(c)
