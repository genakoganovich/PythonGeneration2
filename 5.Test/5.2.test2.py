def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def run():
    n = int(input())
    m = read_matrix_rows(n)
    max_value = m[0][~0]
    for i in range(n):
        for j in range(n):
            if (j >= i >= n - 1 - j) or (i >= j and i >= n - 1 - j):
                if m[i][j] > max_value:
                    max_value = m[i][j]
    print(max_value)


run()
