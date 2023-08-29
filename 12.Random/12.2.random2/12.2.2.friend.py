import random

n = int(input())
students = [input() for _ in range(n)]
friends = students[::]
while any(s == f for s, f in zip(students, friends)):
    random.shuffle(friends)

list(map(lambda s, f: print(f'{s} - {f}'), students, friends))
