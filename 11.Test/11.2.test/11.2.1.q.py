dna = 'GCTA'
rna = 'CGAU'

d = dict(zip(dna, rna))
list(map(lambda x: print(d[x], end=''), input()))
