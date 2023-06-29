import math


def pascal_factor(n, m):
    return int(math.factorial(n) / (math.factorial(m) * math.factorial(n - m)))


def pascal_row(n):
    return [pascal_factor(n, i) for i in range(0, n + 1)]


def pascal(n):
    for i in range(n):
        print(*pascal_row(i))


pascal(int(input()))
