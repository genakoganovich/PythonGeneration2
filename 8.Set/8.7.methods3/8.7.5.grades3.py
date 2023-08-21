grades_1, grades_2, grades_3 = [set(map(int, input().split())) for _ in range(3)]
print(*sorted((grades_3 - grades_1) & (grades_3 - grades_2), reverse=True))
