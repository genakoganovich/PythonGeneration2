with open('lines.txt', encoding='utf-8') as file:
    lines = list(map(str.strip, file.readlines()))


max_length = max(map(len, lines))
list(map(lambda x: print(x), filter(lambda x: len(x) == max_length, lines)))
