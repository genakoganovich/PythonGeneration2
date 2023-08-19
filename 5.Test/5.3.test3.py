def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def run():
    n = int(input())
    m = read_matrix_rows(n)
    list(map(lambda x: print(*x), zip(*m)))


run()
