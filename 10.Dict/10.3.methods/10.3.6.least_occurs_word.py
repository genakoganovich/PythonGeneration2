import re

words = re.sub(r'[.,!?:;-]', '', input().lower()).split()
d = {key: words.count(key) for key in set(words)}
min_count = min(d.values())
print(sorted(filter(lambda x: d[x] == min_count, d))[0])