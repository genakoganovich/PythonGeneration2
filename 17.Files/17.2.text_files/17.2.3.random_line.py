import random

file_name = 'lines.txt'
file = open(file_name)
print(random.choice(file.readlines()))
file.close()
