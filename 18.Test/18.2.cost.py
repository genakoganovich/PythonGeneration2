with open('ledger.txt', encoding='utf-8') as file:
    lines = list(map(str.rstrip, file.readlines()))

print(f'${sum([int(x[1:]) for x in lines])}')
