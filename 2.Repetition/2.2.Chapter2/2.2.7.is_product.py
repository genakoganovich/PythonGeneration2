def is_product(numbers, k):
    return any(i != j and numbers[i] * numbers[j] == k for i in range(len(numbers)) for j in range(len(numbers)))


print('ДА' if is_product([int(input()) for _ in range(int(input()))], int(input())) else 'НЕТ')
