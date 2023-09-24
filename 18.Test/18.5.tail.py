with open(input(), encoding='utf-8') as file:
    lines = list(map(str.rstrip, file.readlines()))

list(map(lambda x: print(x), lines[~9:]))
