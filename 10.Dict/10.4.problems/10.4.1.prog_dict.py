n = int(input())
word_def = {str(x[0]).lower(): x[1] for x in [input().split(': ') for _ in range(n)]}
m = int(input())
list(map(lambda x: print(x), [word_def.get(input().lower(), 'Не найдено') for _ in range(m)]))
