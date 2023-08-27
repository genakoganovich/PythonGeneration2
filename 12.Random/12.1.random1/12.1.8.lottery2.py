import random

beg, end, total = (1000000, 10000000, 100)
for num in random.sample(range(beg, end), total):
    print(num)
