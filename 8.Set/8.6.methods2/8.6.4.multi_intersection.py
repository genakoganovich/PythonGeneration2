n = int(input())
number_1, *other_numbers = [set(input()) for _ in range(n)]
print(*sorted(set(number_1).intersection(*other_numbers)))
