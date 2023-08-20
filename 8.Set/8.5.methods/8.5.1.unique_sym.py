n = int(input())
words = [input() for _ in range(n)]
list(map(lambda x: print(len(set(str(x).lower()))), words))
