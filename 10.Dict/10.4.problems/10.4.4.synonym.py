n = int(input())
d = dict(input().split() for _ in range(n))
d_rev = {value: key for key, value in d.items()}
d.update(d_rev)
print(d[input()])
