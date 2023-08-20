import re

words = re.sub('[.,;:?!-]', '', input().lower()).split()
print(len(set(words)))
