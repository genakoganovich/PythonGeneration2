n = int(input())
number_name = [input().lower().split() for _ in range(n)]
d = {name: list(map(lambda x: x[0], filter(lambda x: x[1] == name, number_name))) for number, name in number_name}
m = int(input())
list(map(lambda x: print(*d.get(x.lower(), ['абонент не найден'])), [input() for _ in range(m)]))
