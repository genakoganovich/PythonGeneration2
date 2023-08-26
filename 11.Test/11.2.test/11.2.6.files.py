access = {'execute': 'X', 'read': 'R', 'write': 'W'}
n = int(input())
d = {x[0]: x[1:] for x in [input().split() for _ in range(n)]}

m = int(input())
query = [(name, access[action]) for action, name in [input().split() for _ in range(m)]]

for name, action in query:
    print('OK' if name in d and action in d[name] else 'Access denied')
