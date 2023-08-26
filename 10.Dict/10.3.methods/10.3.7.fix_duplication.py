words = input().split()
d = dict.fromkeys(words, 0)
result = list()

for w in words:
    result.append(f'{w}_{d[w]}' if d[w] else w)
    d[w] += 1

print(*result)
