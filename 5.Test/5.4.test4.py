def run():
    n = int(input())
    m = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == n // 2 or j == n // 2 or i == j or j == n - i - 1:
                m[i][j] = '*'
    list(map(lambda x: print(*x), m))


run()
