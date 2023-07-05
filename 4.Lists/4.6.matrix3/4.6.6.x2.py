def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def is_in(i, j, n):
    return i <= j and i <= n - 1 - j or i >= j and i >= n - 1 - j


def run(n):
    print_matrix([[[0, 1][is_in(i, j, n)] for j in range(n)] for i in range(n)])


run(int(input()))
