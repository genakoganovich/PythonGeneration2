weight, height = map(float, [input() for _ in range(2)])

bmi = weight / (height * height)
print('Недостаточная масса' if bmi < 18.5 else 'Оптимальная масса' if bmi <= 25 else 'Избыточная масса')
