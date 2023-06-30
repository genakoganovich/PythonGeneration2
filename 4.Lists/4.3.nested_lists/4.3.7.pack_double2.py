import re

s = input().replace(' ', '')
print(s)
print(re.findall(r'(\w)\1+', s))
