from decimal import *
num = Decimal(input())

digits = list(num.as_tuple().digits)

if abs(num) < 1:
    digits.append(0)

print(sum([min(digits), max(digits)]))
