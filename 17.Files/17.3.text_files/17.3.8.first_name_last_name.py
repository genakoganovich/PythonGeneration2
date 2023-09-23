import random

with open('first_names.txt', encoding='utf-8') as file_first, open('last_names.txt', encoding='utf-8') as file_last:
    first_names = list(map(str.rstrip, file_first.readlines()))
    last_names = list(map(str.rstrip, file_last.readlines()))

for _ in range(3):
    print(random.choice(first_names), random.choice(last_names))
