def get_dict(word):
    return {key: word.count(key) for key in set(word)}


print('YES' if get_dict(input()) == get_dict(input()) else 'NO')
