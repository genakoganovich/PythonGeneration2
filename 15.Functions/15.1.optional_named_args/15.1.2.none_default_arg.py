def append(element, seq=None):
    if seq is None:
        seq = []
    seq.append(element)
    return seq


print(append(10))
print(append(5))
print(append(1))
