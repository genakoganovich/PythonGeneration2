from functools import reduce
from operator import add


def evaluate(coefficients, x):
    n = len(coefficients)
    return reduce(add, map(lambda a, i: a * pow(x, i), coefficients, range(n - 1, -1, -1)), 0)


def run():
    coefficients = list(map(int, input().split()))
    x = int(input())
    print(evaluate(coefficients, x))


run()
