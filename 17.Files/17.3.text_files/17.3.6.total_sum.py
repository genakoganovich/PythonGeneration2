import functools
import operator
import re

with open('nums.txt', encoding='utf-8') as file:
    print(functools.reduce(operator.add, map(int, re.findall(r'\d+', file.read()))))
