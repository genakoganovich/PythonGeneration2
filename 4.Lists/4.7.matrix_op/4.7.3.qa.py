import numpy as np

a = np.array([1, -1, 0, 3, -4, 2]).reshape((2, 3))
b = np.arange(1, 7).reshape((3, 2))

print(a)
print(b)
print(np.matmul(a, b))
