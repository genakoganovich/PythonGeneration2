import math


def print_winner(moves):
    weapon = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']
    winner = ['Тимур', 'Руслан', 'ничья']
    print(winner[math.ceil((weapon.index(moves[1]) - weapon.index(moves[0])) % len(weapon) / 2)])


print_winner([input() for _ in range(2)])
