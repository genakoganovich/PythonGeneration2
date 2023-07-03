import numpy as np


def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n):
    print_matrix(np.flipud(np.array(read_matrix_rows(n))))


run(int(input()))
