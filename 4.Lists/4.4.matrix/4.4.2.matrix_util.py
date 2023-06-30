def print_matrix_n(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def print_matrix_n_m(matrix, n, m, width=1):
    for r in range(n):
        for c in range(m):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def read_square_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def read_square_matrix_elements(n):
    return [[input() for _ in range(n)] for _ in range(n)]


def read_matrix_elements(n, m):
    return [[input() for _ in range(m)] for _ in range(n)]


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def transpose_matrix_zip(matrix):
    return zip(*matrix)


def get_trace(matrix):
    return sum([matrix[i][i] for i in range(len(matrix))])


def select(matrix, predicate):
    return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix)) if predicate(i, j)]