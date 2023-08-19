s = input().split()
n = int(input())
print([s[i: len(s) + 1: n] for i in range(n)])
