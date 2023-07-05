def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n, m):
    print_matrix([range(1 + m * i, m * (i + 1) + 1)[::(-1) ** i] for i in range(n)], 3)


run(*(map(int, input().split())))
