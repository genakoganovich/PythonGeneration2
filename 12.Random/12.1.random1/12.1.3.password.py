import random

length = int(input())    # длина пароля
bounds = [(65, 90), (97, 122)]

for _ in range(length):
    choice = random.randint(0, 1)
    print(chr(random.randint(bounds[choice][0], bounds[choice][1])), end='')
