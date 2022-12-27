import numpy as np

array = np.random.uniform(size=(8, 8))

print(array)

array[:, -1] = array[:, -1] + 10

print("\n\n")
print(array)