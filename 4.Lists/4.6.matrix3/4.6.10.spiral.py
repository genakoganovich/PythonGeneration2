import numpy as np


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def populate_matrix(matrix):

    return matrix


def run(n, m):
    print_matrix(populate_matrix([[0] * m for _ in range(n)]), 3)


# run(*(map(int, input().split())))

matrix = np.array(np.arange(12).reshape((3, 4)))
while matrix.size:
    print(matrix)
    if min(matrix.shape) > 1:
        for _ in range(3):
            matrix = np.rot90(matrix)
            print(matrix)

    matrix = matrix[1:-1, 1:-1]
