import numpy as np

array = np.arange(9, dtype=np.float32).reshape(3, 3)

array = array.astype(int)

print(array)