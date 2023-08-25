n = int(input())
cities = [input() for _ in range(n)]
print('REPEAT' if input() in cities else 'OK')
