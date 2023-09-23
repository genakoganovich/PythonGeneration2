def read_csv():
    file_name = 'data.csv'
    with open(file_name, encoding='utf-8') as file:
        keys = file.readline().rstrip().split(',')
        values = list(map(str.rstrip, file.readlines()))

    return [dict(zip(keys, v.split(','))) for v in values]

