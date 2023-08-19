n = 8
board = [['.'] * n for _ in range(n)]

pos = input()
v = n - (ord(pos[1]) - ord('1')) - 1
h = ord(pos[0]) - ord('a')


for i in range(n):
    for j in range(n):
        if i == v or j == h or abs(i - v) == abs(j - h):
            board[i][j] = '*'

board[v][h] = 'Q'
list(map(lambda x: print(*x), board))
