def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def is_latin_row(row, n):
    return all(i in row for i in range(1, n + 1))


def is_latin_square(matrix, n):
    return all(is_latin_row(row, n) for row in matrix) and all(is_latin_row(row, n) for row in zip(*matrix))


def run():
    n = int(input())
    matrix = read_matrix_rows(n)
    print('YES' if is_latin_square(matrix, n) else 'NO')


run()
