import random

n = int(input())
for _ in range(n):
    print('Орел' if random.randint(0, 1) else 'Решка')
