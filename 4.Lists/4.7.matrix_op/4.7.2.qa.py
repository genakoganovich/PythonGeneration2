import numpy as np
a = np.array([np.ones(3, dtype=int), np.ones(3, dtype=int) * 2, np.ones(3, dtype=int) * 3])
b = np.arange(1, 10).reshape((3, 3))
print(a)
print(b)
print(np.matmul(a, b))
