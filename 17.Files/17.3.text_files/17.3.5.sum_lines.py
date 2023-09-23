import functools
import operator

with open('numbers.txt', encoding='utf-8') as file:
    lines = list(map(str.strip, file.readlines()))


list(map(lambda x: print(sum(map(int, str(x).split()))), lines))
