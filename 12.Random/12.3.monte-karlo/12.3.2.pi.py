import random

n = 10 ** 6  # количество испытаний
a, b = (-1, 1)


def get_circle(x, y):
    return x ** 2 + y ** 2


def run():
    k = 0
    for _ in range(n):
        x = a + (b - a) * random.random()
        y = a + (b - a) * random.random()
        if get_circle(x, y) <= 1:
            k += 1
    print(k * ((b - a) ** 2) / n)


run()
