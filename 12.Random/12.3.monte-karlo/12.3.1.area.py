import random

n = 10 ** 6  # количество испытаний
a, b = (-2, 2)


def func_1(x, y):
    return x ** 3 + y ** 4 + 2


def func_2(x, y):
    return 3 * x + y ** 2


def run():
    k = 0
    for _ in range(n):
        x = a + (b - a) * random.random()
        y = a + (b - a) * random.random()
        if func_1(x, y) >= 0 and func_2(x, y) <= 2:
            k += 1
    print(k * ((b - a) ** 2) / n)


run()
