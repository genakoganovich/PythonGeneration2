def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def is_symmetrical(m):
    for i in range(len(m)):
        for j in range(len(m) - i - 1):
            if m[i][j] != m[~j][~i]:
                return False
    return True


def run():
    n = int(input())
    m = read_matrix_rows(n)
    print('YES' if is_symmetrical(m) else 'NO')


run()
