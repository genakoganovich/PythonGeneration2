import numpy as np


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n):
    matrix_one = np.ones((n, n), int)
    matrix_eye = np.fliplr(np.eye(n, dtype=int))
    print_matrix(matrix_eye + np.fliplr(np.tril(matrix_one, k=-1) * 2))


run(int(input()))
