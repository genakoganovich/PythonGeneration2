from fractions import Fraction as F
import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

a, b = [input() for _ in range(2)]
list(map(lambda k, v: print(f'{a} {k} {b} = {v(F(a), F(b))}'), ops.keys(), ops.values()))
