def read_matrix_elements(n, m):
    return [[input() for _ in range(m)] for _ in range(n)]


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def run(n, m):
    matrix = read_matrix_elements(n, m)
    print_matrix(matrix)
    print()
    print_matrix(transpose_matrix(matrix))


run(int(input()), int(input()))
