def replace_last(t):
    t = list(t)
    t[~0] = 100
    return tuple(t)


tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [replace_last(x) for x in tuples]
print(new_tuples)
