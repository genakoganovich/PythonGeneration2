digits = list(map(int, input().split()))
unique_digits = set()
unique_digits_len = len(unique_digits)

for d in digits:
    unique_digits.add(d)
    print('YES' if len(unique_digits) == unique_digits_len else 'NO')
    unique_digits_len = len(unique_digits)
