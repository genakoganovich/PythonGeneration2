import functools
import operator
import re

with open('forbidden_words.txt', encoding='utf-8') as file:
    lines = list(map(str.rstrip, file.readlines()))

words = sorted(functools.reduce(operator.add, map(str.split, lines)), key=len, reverse=True)

with open(input(), encoding='utf-8') as file:
    text = file.read()

for w in words:
    text = re.sub(w, '*' * len(w), text, flags=re.IGNORECASE)

print(text)
