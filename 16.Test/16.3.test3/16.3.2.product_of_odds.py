import functools


def product_of_odds_old(data):  # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result


def product_of_odds(data):
    return functools.reduce(lambda a, b: a * b, filter(lambda x: x % 2, data), 1)


lst = [1, 3, 5]

print(product_of_odds_old(lst))
print(product_of_odds(lst))
