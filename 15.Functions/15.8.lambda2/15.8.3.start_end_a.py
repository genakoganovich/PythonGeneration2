func = lambda x: str(x[0]).lower() == 'a' and str(x[~0]).lower() == 'a'

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))