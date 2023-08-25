words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_word = dict(zip(map(str, range(10)), words))
list(map(lambda x: print(num_word[x], end=' '), input()))
