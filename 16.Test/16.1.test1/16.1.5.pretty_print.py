def pretty_print(data, side='-', delimiter='|'):
    line = f' {delimiter} '.join(map(str, data))
    print('', side * (len(line) + 2))
    print(delimiter, line, delimiter)
    print('', side * (len(line) + 2))

