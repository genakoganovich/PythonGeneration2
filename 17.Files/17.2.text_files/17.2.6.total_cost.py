import functools
import operator

file_name = 'prices.txt'
file = open(file_name, encoding='utf-8')

print(functools.reduce(operator.add,
                       map(lambda x: int(x[1]) * int(x[2]), map(str.split, map(str.rstrip, file.readlines()))),
                       0))

file.close()
