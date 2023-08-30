import string
import re
import random

symbols_to_remove, *_ = ('lI1oO0',)
symbols = re.sub(rf'[{symbols_to_remove}]', '', string.ascii_letters + string.digits)


def generate_password(length):
    return random.sample(symbols, length)


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())

list(map(lambda x: print(''.join(x)), generate_passwords(n, m)))
