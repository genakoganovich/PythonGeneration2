import random

n = int(input())
students = [input() for _ in range(n)]

for i in range(n):
    print(random.choice(students[:i] + students[i + 1:]))
