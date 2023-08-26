n = int(input())
d = {}
for _ in range(n):
    state, *cities = input().split()
    d.update(dict.fromkeys(cities, state))

m = int(input())
list(map(lambda x: print(d[x]), [input() for _ in range(m)]))
