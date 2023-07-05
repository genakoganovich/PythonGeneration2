import numpy as np


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n, m):
    print_matrix(np.arange(1, n * m + 1).reshape((n, m)), 3)


run(*[int(x) for x in input().split()])
