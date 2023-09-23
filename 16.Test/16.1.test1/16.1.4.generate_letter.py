def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    letter = [f'To: {mail}',
              f'Приветствую, {name}!',
              f'Вам назначен экзамен, который пройдет {date}, в {time}.',
              f'По адресу: {place}.',
              f'Экзамен будет проводить {teacher} в кабинете {number}.',
              'Желаем удачи на экзамене!'
              ]
    return '\n'.join(letter)
