m, n = map(int, [input() for _ in range(2)])
names = set()
for _ in range(m + n):
    student = input()
    if student in names:
        names.remove(student)
    else:
        names.add(student)

print(len(names) if names else 'NO')
