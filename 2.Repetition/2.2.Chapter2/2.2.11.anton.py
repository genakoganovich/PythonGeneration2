import re

for i in range(1, int(input()) + 1):
    if re.search(r'.*a.*n.*t.*o.*n.*', input()):
        print(i, end=' ')
