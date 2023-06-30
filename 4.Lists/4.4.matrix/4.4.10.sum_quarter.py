def read_square_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def select(matrix, predicate):
    return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix)) if predicate(len(matrix), i, j)]


def run(matrix):
    names = ['Верхняя', 'Правая', 'Нижняя', 'Левая']
    areas = [lambda length, i, j: i < j and i < length - 1 - j, lambda length, i, j: j > i > length - 1 - j,
             lambda length, i, j: i > j and i > length - 1 - j, lambda length, i, j: j < i < length - 1 - j]

    for name, area in zip(names, areas):
        print(f'{name} четверть:', sum(select(matrix, area)))


run(read_square_matrix_rows(int(input())))
