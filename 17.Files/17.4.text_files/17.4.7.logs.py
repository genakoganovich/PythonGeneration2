from datetime import datetime


def was_long(line, more):
    *_, beg, end = str(line).split(', ')
    from_time = datetime.strptime(beg, '%H:%M')
    to_time = datetime.strptime(end, '%H:%M')
    return (to_time - from_time).total_seconds() / 3600 >= more


def run():
    with open('logfile.txt', encoding='utf-8') as file_in:
        lines = list(map(str.rstrip, file_in.readlines()))
    with open('output.txt', 'w', encoding='utf-8') as file_out:
        list(map(lambda x: print(str(x).split(', ')[0], file=file_out), filter(lambda x: was_long(x, 1), lines)))


run()
