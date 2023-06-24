numbers = list(map(int, input().split()))

print(sum([1 for i in range(len(numbers) - 1) if numbers[i] < numbers[i + 1]]))
