def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n, m):
    print_matrix([[i * j for i in range(m)] for j in range(n)], 3)


run(int(input()), int(input()))
