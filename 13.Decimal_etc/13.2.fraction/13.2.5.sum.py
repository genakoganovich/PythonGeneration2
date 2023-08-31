from fractions import Fraction as F

n = int(input())
s = F(0)
for i in range(1, n + 1):
    s += F(1, i**2)
print(s)
