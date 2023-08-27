import random

length, beg, end = (7, 1, 49)
lottery = set()
while len(lottery) < length:
    lottery.add(random.randint(beg, end))
print(*sorted(lottery))
