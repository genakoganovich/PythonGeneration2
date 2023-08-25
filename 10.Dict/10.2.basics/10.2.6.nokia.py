keyboard = [" ", ".,?!:", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
symbols = ''.join(keyboard)
d = dict(zip(map(str, range(10)), keyboard))

word = input().upper()
res = [key * (list(value).index(c) + 1) for c in word for key, value in d.items() if c in symbols and c in value]
print(*res, sep='')
