text = input().split()
res = [[]]

for i in range(len(text)):
    for j in range(len(text) - i):
        res.append(text[j:j + i + 1])
print(res)
