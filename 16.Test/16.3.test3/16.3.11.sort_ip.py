import functools


def sum_octets(x):
    octets = list(map(int, str(x).split('.')))
    return functools.reduce(lambda a, b: a + b, map(lambda a, b: a * 256 ** b, octets, range(4, -1, -1)), 0)


def run():
    n = int(input())
    ips = [input() for _ in range(n)]
    list(map(lambda x: print(x), sorted(ips, key=sum_octets)))


run()
