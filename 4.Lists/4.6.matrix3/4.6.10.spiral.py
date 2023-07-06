def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def populate_matrix(matrix):
    count = 0
    for offset in range(len(matrix) - 1, -len(matrix[0]), -1):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i + j + 1 == len(matrix) - offset:
                    count += 1
                    matrix[i][j] = count
    return matrix


def run(n, m):
    print_matrix(populate_matrix([[0] * m for _ in range(n)]), 3)


run(*(map(int, input().split())))
