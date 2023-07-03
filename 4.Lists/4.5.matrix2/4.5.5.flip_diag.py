import numpy as np


def flip_diagonals(arr):
    diagonal = arr.diagonal().copy()
    anti_diagonal = np.fliplr(arr).diagonal().copy()
    np.fill_diagonal(np.flipud(arr), diagonal)
    np.fill_diagonal(np.flipud(np.fliplr(arr)), anti_diagonal)


def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n):
    a = np.array(read_matrix_rows(n))
    flip_diagonals(a)
    print_matrix(a)


run(int(input()))
