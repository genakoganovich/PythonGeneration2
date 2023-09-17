n = int(input())
grades = list()
for _ in range(n):
    k = int(input())
    grades.append(any(map(lambda x: x == 5, [int(input().split()[1]) for _ in range(k)])))

print('YES' if all(grades) else 'NO')
