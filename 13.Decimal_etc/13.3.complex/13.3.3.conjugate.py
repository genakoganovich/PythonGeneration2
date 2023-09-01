def func(z1, z2, n):
    return z1 ** n + z2 ** n + complex(z1).conjugate() ** n + complex(z2).conjugate() ** (n + 1)


def run():
    n = int(input())
    z1, z2 = (complex(input()) for _ in range(2))
    print(func(z1, z2, n))


run()
