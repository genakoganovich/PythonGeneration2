n = int(input())
words = [input().lower() for _ in range(n)]
print(len(set(''.join(words))))
