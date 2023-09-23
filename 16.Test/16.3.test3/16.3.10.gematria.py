n = int(input())
words = [input() for _ in range(n)]

list(map(lambda x: print(x), sorted(words, key=lambda w: (sum(map(lambda x: ord(str(x).upper()) - ord('A'), w)), w))))
