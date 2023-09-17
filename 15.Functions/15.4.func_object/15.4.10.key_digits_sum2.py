print(*sorted(sorted(input().split(), key=int), key=lambda x: sum(map(int, x))))
