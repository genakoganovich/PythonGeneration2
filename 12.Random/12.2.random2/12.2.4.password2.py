import string
import re
import random

symbols_to_remove, *_ = ('lI1oO0',)

ascii_lowercase = re.sub(rf'[{symbols_to_remove}]', '', string.ascii_lowercase)
ascii_uppercase = re.sub(rf'[{symbols_to_remove}]', '', string.ascii_uppercase)
digits = re.sub(rf'[{symbols_to_remove}]', '', string.digits)


def get_length(length):
    return length // 3, length // 3, length - 2 * length // 3


def generate_password_lowercase(length):
    return random.sample(ascii_lowercase, length)


def generate_password_uppercase(length):
    return random.sample(ascii_uppercase, length)


def generate_password_digits(length):
    return random.sample(digits, length)


def generate_password(length):
    length_lowercase, length_uppercase, length_digits = get_length(length)
    result = (generate_password_lowercase(length_lowercase) +
              generate_password_uppercase(length_uppercase) +
              generate_password_digits(length_digits))
    random.shuffle(result)
    return result


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())

list(map(lambda x: print(''.join(x)), generate_passwords(n, m)))
