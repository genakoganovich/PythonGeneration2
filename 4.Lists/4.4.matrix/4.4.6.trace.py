def read_square_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def get_trace(matrix):
    return sum([matrix[i][i] for i in range(len(matrix))])


def run(n):
    print(get_trace(read_square_matrix_rows(n)))


run(int(input()))
