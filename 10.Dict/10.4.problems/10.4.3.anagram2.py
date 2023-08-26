import re


def get_dict(word):
    return {key: word.count(key) for key in set(word)}


def process(word):
    return re.sub(r'[ .,!?:;-]', '', str(word).lower())


print('YES' if get_dict(process(input())) == get_dict(process(input())) else 'NO')
