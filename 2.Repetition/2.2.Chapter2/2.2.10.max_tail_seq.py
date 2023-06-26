import re

print(max(map(len, ([''] + re.findall(r'Р+', input())))))
