def print_matrix(matrix, width=1):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


def get_j(pos):
    return ord(pos[0]) - ord('a')


def get_i(pos):
    return ord('8') - ord(pos[1])


def is_in(x, y):
    return -1 < x < 8 and -1 < y < 8


def populate_chessboard(chessboard, x, y):
    chessboard[x][y] = 'N'
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) + abs(j) == 3 and is_in(x + i, y + j):
                chessboard[x + i][y + j] = '*'
    return chessboard


def create_chessboard():
    return [['.'] * 8 for _ in range(8)]


def run(pos):
    chessboard = create_chessboard()
    chessboard = populate_chessboard(chessboard, get_i(pos), get_j(pos))
    print_matrix(chessboard)


run(input())
