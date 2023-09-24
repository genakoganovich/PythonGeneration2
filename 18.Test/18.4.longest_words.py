import functools
import operator

with open('words.txt', encoding='utf-8') as file:
    lines = list(map(str.rstrip, file.readlines()))

words = functools.reduce(operator.add, map(str.split, lines))
max_len = max(map(len,  words))
list(map(lambda x: print(x), filter(lambda x: len(x) == max_len, words)))
