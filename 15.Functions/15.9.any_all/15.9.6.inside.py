r = 2

abscissas, ordinates, applicates = [list(map(float, input().split())) for _ in range(3)]
print(all(map(lambda x, y, z: x ** 2 + y ** 2 + z ** 2 <= r ** 2, abscissas, ordinates, applicates)))

