def read_square_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def select(matrix, predicate):
    return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix)) if predicate(i, j)]


def get_area(n, i, j):
    return j <= i <= n - 1 - j or j >= i >= n - 1 - j


def get_max_area(matrix):
    return max(select(matrix, lambda i, j: get_area(len(matrix), i, j)))


def run(n):
    print(get_max_area(read_square_matrix_rows(n)))


run(int(input()))
