set_1, set_2 = [set(input()) for _ in range(2)]
print('YES' if set(set_1).issuperset(set_2) else 'NO')
