import random
import string


def get_letter():
    return random.choice(string.ascii_uppercase)


def get_number():
    return str(random.choice(range(100)))


def generate_index():
    left = f'{get_letter()}{get_letter()}{get_number()}'
    right = f'{get_number()}{get_letter()}{get_letter()}'
    return '_'.join([left, right])
