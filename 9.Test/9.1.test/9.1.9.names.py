manager_set = set(input().split())
assistant_set = set(input().split())
print(*sorted(manager_set | assistant_set))
