m = int(input())
n = int(input())
home_books = set([input() for _ in range(m)])
for _ in range(n):
    print('YES' if input() in home_books else 'NO')
