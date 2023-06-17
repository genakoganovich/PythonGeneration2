animals = ['Дракон',  'Змея',  'Лошадь',  'Овца',  'Обезьяна',  'Петух',  'Собака',
           'Свинья',  'Крыса',  'Бык',  'Тигр',  'Заяц']

chinese_calendar = {i: animals[i] for i in range(len(animals))}
print(chinese_calendar[(int(input()) - 2000) % 12])
