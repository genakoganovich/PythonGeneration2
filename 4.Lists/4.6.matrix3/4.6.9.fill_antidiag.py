import numpy as np


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n, m):
    print_matrix([range(1 + m * i, m * (i + 1) + 1)[::(-1) ** i] for i in range(n)], 3)


# run(*(map(int, input().split())))

matrix = [[1, 2, 4, 7, 10], [3, 5, 8, 11, 13], [6, 9, 12, 14, 15]]
print_matrix(matrix, 3)

for i in range(4, -3, -1):
    print(np.fliplr(matrix).diagonal(offset=i))
