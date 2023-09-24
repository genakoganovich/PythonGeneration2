min_grade = 65

with open('grades.txt', encoding='utf-8') as file:
    lines = map(str.split, map(str.rstrip, file.readlines()))

grades = map(lambda x: x[1:], lines)
print(len(list(filter(lambda x: all(map(lambda t: int(t) >= min_grade, x)), grades))))
