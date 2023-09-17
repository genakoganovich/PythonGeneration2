a, b = [int(input()) for _ in range(2)]
print(*filter(lambda x: all(map(int, str(x))) and all((map(lambda y: not x % int(y), str(x)))), range(a, b + 1)))
