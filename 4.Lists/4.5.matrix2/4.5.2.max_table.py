import numpy as np


def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n, m):
    a = np.array(read_matrix_rows(n))
    ind = np.unravel_index(np.argmax(a, axis=None), a.shape)
    print(*ind)


run(int(input()), int(input()))
