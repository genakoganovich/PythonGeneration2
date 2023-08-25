m, n = map(int, [input() for _ in range(2)])
math_names = set(input() for _ in range(m))
cs_names = set(input() for _ in range(n))
print(len(math_names - cs_names))
