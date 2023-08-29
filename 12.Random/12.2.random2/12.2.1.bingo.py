import numpy as np
import random
beg, end, mid, size = (1, 76, 12, 5)

m = random.sample(range(beg, end), size * size)
m[mid] = 0
m = np.reshape(m, (size, size))

for row in m:
    for x in row:
        print(str(x).ljust(3), end=' ')
    print()
