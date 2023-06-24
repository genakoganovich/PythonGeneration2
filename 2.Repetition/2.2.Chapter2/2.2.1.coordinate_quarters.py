quarters = ['Первая четверть', 'Вторая четверть', 'Третья четверть', 'Четвертая четверть']
count = {q : 0 for q in quarters}


for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        count[quarters[0]] += 1
    elif x < 0 and y > 0:
        count[quarters[1]] += 1
    elif x < 0 and y < 0:
        count[quarters[2]] += 1
    elif x > 0 and y < 0:
        count[quarters[3]] += 1

for k, v in count.items():
    print(f'{k}: {v}')
