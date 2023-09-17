nums = input().split()
print(*sorted(nums, key=lambda x: sum(map(int, x))))
