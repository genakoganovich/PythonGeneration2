text = input().split()
d = dict.fromkeys(text, 1)
for s in text:
    print(d[s], end=' ')
    d[s] += 1
