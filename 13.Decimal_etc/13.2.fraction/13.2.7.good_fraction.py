import math
from fractions import Fraction as F

n = int(input())
good_fractions = set([F(i, j) for i in range(1, n + 1) for j in range(1, n + 1) if i < j and i + j == n])
good_fractions = set(filter(lambda x: F(x).numerator + F(x).denominator == n, good_fractions))
print(max(good_fractions))
