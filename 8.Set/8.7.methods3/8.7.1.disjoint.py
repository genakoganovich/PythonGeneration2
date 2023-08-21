set_1, set_2 = [set(input()) for _ in range(2)]
print('NO' if set(set_1).isdisjoint(set_2) else 'YES')
