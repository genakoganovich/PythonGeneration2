n = int(input())
d = {}

for _ in range(n):
    name, item, quantity = input().split()
    d.setdefault(name, {}).setdefault(item, []).append(int(quantity))

for name in sorted(d):
    print(f'{name}:')
    for item in sorted(d[name]):
        print(f'{item} {sum(d[name][item])}')
