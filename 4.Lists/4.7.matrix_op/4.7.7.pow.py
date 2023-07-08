import numpy as np


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def read_matrix_rows(n, m=1):
    return [list(map(int, input().split())) for _ in range(n)]


def pow_matrix(matrix, k):
    result = np.eye(matrix.shape[0], dtype=int)
    for _ in range(k):
        result = np.matmul(result, matrix)
    return result


def run():
    a = np.array(read_matrix_rows(int(input())))
    print_matrix(pow_matrix(a, int(input())))


run()
