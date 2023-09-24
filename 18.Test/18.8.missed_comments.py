def get_name(s):
    return s[:str(s).find('(')]


with open(input(), encoding='utf-8') as file:
    lines = file.readlines()

not_commented = list()

if lines[0].startswith('def '):
    not_commented.append(get_name(lines[0].split()[1]))

for i in range(1, len(lines)):
    if lines[i].startswith('def ') and not lines[i - 1].startswith('#'):
        not_commented.append(get_name(lines[i].split()[1]))

if not_commented:
    list(map(lambda x: print(x), not_commented))
else:
    print('Best Programming Team')
