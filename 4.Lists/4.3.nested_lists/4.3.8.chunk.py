def chunked(s, n):
    return [list(s[i: i + n]) for i in range(0, len(s), n)]


print(chunked(input().replace(' ', ''), int(input())))
