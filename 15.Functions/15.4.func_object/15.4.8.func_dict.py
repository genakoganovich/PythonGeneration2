import math

names = ['квадрат', 'куб', 'корень', 'модуль', 'синус']
func = [lambda x: x ** 2, lambda x: x ** 3, math.sqrt, abs, math.sin]
d = dict(zip(names, func))

value = int(input())
print(d[input()](value))
