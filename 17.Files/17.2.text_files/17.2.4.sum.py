import functools
import operator

file_name = 'numbers.txt'
file = open(file_name)

print(functools.reduce(operator.add, map(int, map(str.rstrip, file.readlines()))))
file.close()
