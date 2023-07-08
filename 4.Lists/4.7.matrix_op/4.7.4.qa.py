import numpy as np

a = np.array([1, 0, 4, 1]).reshape((2, 2))

m = np.eye(2, dtype=int)

for _ in range(25):
    m = np.matmul(m, a)
    print(m)



