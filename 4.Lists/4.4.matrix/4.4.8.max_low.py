def read_square_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def select(matrix, predicate):
    return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix)) if predicate(i, j)]


def get_max_low(matrix):
    return max(select(matrix, lambda x, y: x >= y))


def run(n):
    print(get_max_low(read_square_matrix_rows(n)))


run(int(input()))
