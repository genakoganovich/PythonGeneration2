set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
set_3 = set_1 & set_2

print(*sorted(set_3, reverse=True) if len(set_3) else ['BAD DAY'])
