def read_matrix_elements(n, m):
    return [[input() for _ in range(m)] for _ in range(n)]


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n, m):
    print_matrix(read_matrix_elements(n, m))


run(int(input()), int(input()))
