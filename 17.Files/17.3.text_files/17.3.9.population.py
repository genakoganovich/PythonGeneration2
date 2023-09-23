max_population = 500000

with open('population.txt', encoding='utf-8') as file:
    country_population = [str.rstrip(x).split('\t') for x in file.readlines()]

list(map(lambda x: print(x[0]), filter(lambda x: x[0][0] == 'G' and int(x[1]) > max_population, country_population)))
