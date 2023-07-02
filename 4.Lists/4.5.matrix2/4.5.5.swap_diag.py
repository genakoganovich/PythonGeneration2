import numpy as np


def swap_diagonals(arr):
    diagonal = arr.diagonal().copy()
    anti_diagonal = np.fliplr(arr).diagonal().copy()
    np.fill_diagonal(arr, anti_diagonal)
    np.fill_diagonal(np.fliplr(arr), diagonal)


def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n):
    a = np.array(read_matrix_rows(n))
    diagonal = a.diagonal().copy()
    anti_diagonal = np.fliplr(a).diagonal().copy()
    np.fill_diagonal(a, anti_diagonal)
    np.fill_diagonal(np.fliplr(a), diagonal)
    print(diagonal)
    print(anti_diagonal)
    print_matrix(a)


run(int(input()))
