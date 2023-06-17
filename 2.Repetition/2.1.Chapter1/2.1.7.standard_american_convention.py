

def run(string):
    list(map(lambda i: print(string[i], end=',' if len(string[i + 1:]) and not len(string[i + 1:]) % 3 else ''),
             range(len(string))))


run(input())
