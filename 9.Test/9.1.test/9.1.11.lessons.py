m = int(input())
names_set = set(input() for _ in range(int(input())))

for i in range(m - 1):
    names_set &= set(input() for _ in range(int(input())))

print(*sorted(names_set), sep='\n')
