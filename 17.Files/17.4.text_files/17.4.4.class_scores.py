add_value = 5

with open('class_scores.txt') as file_in, open('new_scores.txt', 'w') as file_out:
    for line in file_in:
        name, score = line.rstrip().split()
        file_out.write(f'{name} {min(100, int(score) + add_value)}\n')
