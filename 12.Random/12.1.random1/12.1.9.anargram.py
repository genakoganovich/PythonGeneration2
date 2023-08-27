import random
word = input()
word_list = list(word)
random.shuffle(word_list)
print(''.join(word_list))
