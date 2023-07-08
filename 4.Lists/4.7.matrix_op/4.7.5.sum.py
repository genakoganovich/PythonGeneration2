import numpy as np


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def run(n, m):
    a = read_matrix_rows(n)
    input()
    b = read_matrix_rows(n)
    print_matrix(np.add(a, b))


run(*(map(int, input().split())))