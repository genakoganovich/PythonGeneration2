from fractions import Fraction as F
import math

n = int(input())
result = sorted(set(F(i, j) for j in range(1, n + 1) for i in range(1, n + 1) if i < j and math.gcd(i, j) == 1))
list(map(lambda x: print(x), result))
