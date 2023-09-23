with open('file.txt', encoding='utf-8') as file:
    text = file.read()

lines_count = 1 + text.count('\n')
words_count = len(text.split())
latin_count = len(list(filter(str.isalpha, text)))

print(f'''Input file contains:
{latin_count} letters 
{words_count} words 
{lines_count} lines ''')


