n = int(input())
matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i - j)
list(map(lambda x: print(*x), matrix))
