import numpy as np


def swap_columns(arr, start_index, last_index):
    arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]


def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n, m):
    a = np.array(read_matrix_rows(n))
    swap_columns(a, *list(map(int, input().split())))
    print_matrix(a)


run(int(input()), int(input()))
