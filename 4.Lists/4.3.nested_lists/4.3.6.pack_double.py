s = input().replace(' ', '')

result = list()

curr = s[0]
count = 1
for c in s[1:]:
    if curr == c:
        count += 1
    else:
        result.append([curr] * count)
        count = 1
        curr = c

result.append([curr] * count)
print(result)
