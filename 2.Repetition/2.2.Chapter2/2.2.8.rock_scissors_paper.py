def print_winner(moves):
    weapon = ['камень', 'ножницы', 'бумага']
    winner = ['ничья', 'Тимур', 'Руслан']
    print(winner[weapon.index(moves[1]) - weapon.index(moves[0]) % len(weapon)])


print_winner([input() for _ in range(2)])
