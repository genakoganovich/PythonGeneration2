word = input()
symbol_freq = {c: word.count(c) for c in set(word)}
n = int(input())
letter_freq = {int(x[1]): x[0] for x in [input().split(': ') for _ in range(n)]}
print(''.join(letter_freq[symbol_freq[c]] for c in word))
