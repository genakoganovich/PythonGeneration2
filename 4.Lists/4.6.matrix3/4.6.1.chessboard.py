def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def run(n, m):
    print_matrix([[['.', '*'][(i + j) % 2] for j in range(m)] for i in range(n)])


run(*[int(x) for x in input().split()])
