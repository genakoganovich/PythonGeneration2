import numpy as np


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def read_matrix_rows(n, m=1):
    return [list(map(int, input().split())) for _ in range(n)]


def run():
    a = read_matrix_rows(*(map(int, input().split())))
    input()
    b = read_matrix_rows(*(map(int, input().split())))
    print_matrix(np.matmul(a, b))


run()
