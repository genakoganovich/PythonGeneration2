import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}

z1, z2 = [complex(input()) for _ in range(2)]
list(map(lambda k, v: print(f'{z1} {k} {z2} = {v(z1, z2)}'), ops.keys(), ops.values()))
