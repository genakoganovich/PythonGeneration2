n = int(input())

t1 = t2 = t3 = 1
res = []
for i in range(1, n + 1):
    if i > 3:
        t1, t2, t3 = t2, t3, t1 + t2 + t3
    res.append(t3)

print(*res)
