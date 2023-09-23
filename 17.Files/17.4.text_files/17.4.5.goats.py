threshold = 0.07

with open('goats.txt') as f_in:
    lines = list(map(str.rstrip, f_in.readlines()))

goat_index = lines.index('GOATS')
colors = sorted(lines[1:goat_index])
goats = lines[goat_index + 1:]
total = len(goats)

with open('answer.txt', 'w') as f_out:
    list(map(lambda x: print(x, file=f_out), filter(lambda x: goats.count(x) / total > threshold, colors)))
