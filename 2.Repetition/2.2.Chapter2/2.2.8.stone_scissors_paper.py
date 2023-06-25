def print_winner(timur, ruslan):
    weapon = ['камень', 'ножницы', 'бумага']
    winner = ['Тимур', 'Руслан', 'ничья']
    if (weapon.index(timur) + 1) % 3 == weapon.index(ruslan):
        print(winner[0])
    elif (weapon.index(ruslan) + 1) % 3 == weapon.index(timur):
        print(winner[1])
    else:
        print(winner[2])


print_winner(*[input() for _ in range(2)])