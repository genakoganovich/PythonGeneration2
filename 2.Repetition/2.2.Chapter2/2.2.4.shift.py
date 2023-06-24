numbers = list(map(int, input().split()))
numbers.insert(0, numbers.pop())
print(*numbers)
