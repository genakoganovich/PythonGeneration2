words = input().split()
print('YES' if len(set([''.join(set(x)) for x in words])) == 1 else 'NO')
