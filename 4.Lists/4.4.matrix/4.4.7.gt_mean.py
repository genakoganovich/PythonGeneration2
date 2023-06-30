import statistics as st


def read_square_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def count_gt_mean(matrix):
    return [len(list(filter(lambda x: x > st.mean(row), row))) for row in matrix]


def run(n):
    print(*count_gt_mean(read_square_matrix_rows(n)), sep='\n')


run(int(input()))
