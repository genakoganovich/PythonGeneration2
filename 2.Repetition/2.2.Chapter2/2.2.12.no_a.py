word = f'{input()} запретил букву'

for c in [chr(i) for i in range(1072, 1104)]:
    if c in word:
        print(word, c)
        word = word.replace(c, '').strip().replace('  ', ' ').strip()
