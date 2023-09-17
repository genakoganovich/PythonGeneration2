mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
print(*sorted(mixed_list, key=lambda x: (isinstance(x, str), x)))
