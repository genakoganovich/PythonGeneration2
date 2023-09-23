with open('input.txt') as file_in, open('output.txt', 'w') as file_out:
    for i, line in enumerate(file_in, 1):
        file_out.write(f'{i}) {line}')
