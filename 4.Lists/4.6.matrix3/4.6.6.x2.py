import numpy as np


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def create_matrix(n):
    result = np.fliplr(np.eye(n, dtype=int))
    np.fill_diagonal(result, 1)
    return result


def run(n):
    print_matrix(create_matrix(n))


run(int(input()))
