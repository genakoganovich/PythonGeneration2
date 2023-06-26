def get_winner(i, j):
    return (j - i) % 5 // (1 + (j - i) % 5 // 3)


def print_winner(moves):
    weapon = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']
    winner = ['ничья', 'Тимур', 'Руслан']
    print(winner[get_winner(weapon.index(moves[0]) , weapon.index(moves[1]))])


print_winner([input() for _ in range(2)])
