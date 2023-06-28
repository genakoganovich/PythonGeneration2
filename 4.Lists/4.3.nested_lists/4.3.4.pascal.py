import math


def pascal_factor(n, m):
    return int(math.factorial(n) / (math.factorial(m) * math.factorial(n - m)))


def pascal(n):
    return [pascal_factor(n, i) for i in range(0, n + 1)]


print(pascal(int(input())))
