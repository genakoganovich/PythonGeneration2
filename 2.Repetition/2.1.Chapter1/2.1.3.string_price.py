kopecks = len(input()) * 60
rubles, kopecks = kopecks // 100, kopecks % 100

print(f'{rubles} р. {kopecks} коп.')