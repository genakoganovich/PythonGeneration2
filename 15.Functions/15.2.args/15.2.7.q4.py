def func(*args):
    return max(args) + min(args)


print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))
