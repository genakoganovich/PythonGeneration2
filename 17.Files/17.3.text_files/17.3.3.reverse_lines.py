with open('data.txt', encoding='utf-8') as file:
    lines = map(str.strip, file.readlines()[::-1])

list(map(lambda x: print(x), lines))
