import statistics as st

lst = [1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)]

print(st.mean(list(filter(lambda x: type(x) in [int, float], lst))))
