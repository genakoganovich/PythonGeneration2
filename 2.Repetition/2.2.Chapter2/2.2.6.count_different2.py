values = input().split()
print(1 + sum(values[i] != values[i + 1] for i in range(len(values) - 1)))
