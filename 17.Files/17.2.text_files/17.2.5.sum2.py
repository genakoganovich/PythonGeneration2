import functools
import operator

file_name = 'nums.txt'
file = open(file_name)

print(functools.reduce(operator.add, map(int, map(str.rstrip, file.read().split()))))
file.close()
