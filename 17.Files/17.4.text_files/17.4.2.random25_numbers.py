import random

min_int: int
total_int, min_int, max_int = (25, 111, 777)

with open('random.txt', 'w') as output:
    for _ in range(25):
        output.write(str(random.randint(min_int, max_int)) + '\n')
