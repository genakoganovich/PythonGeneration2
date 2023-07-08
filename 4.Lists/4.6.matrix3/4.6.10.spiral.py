import numpy as np


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def populate_spiral(matrix, value):
    value = populate_edges(matrix, value)

    i = 1
    while matrix[i:-i, i:-i].size:
        value = populate_edges(matrix[i:-i, i:-i], value)
        i += 1

    return matrix


def populate_edges(matrix, value):
    if matrix.shape[0] == 1:
        matrix[0, :] = np.arange(value, value + matrix[0, :].size)
        value += matrix[0, :].size
    elif matrix.shape[1] == 1:
        np.rot90(matrix, 1)[0, :] = np.arange(value, value + np.rot90(matrix, 1)[0, :].size)
        value += np.rot90(matrix, 1)[0, :].size
    else:
        for k in range(4):
            np.rot90(matrix, k)[0, 0:-1] = np.arange(value, value + np.rot90(matrix, k)[0, 0:-1].size)
            value += np.rot90(matrix, k)[0, 0:-1].size
    return value


def run(n, m):
    print_matrix(populate_spiral(np.zeros((n, m), dtype=int), 1), 3)


run(*(map(int, input().split())))
