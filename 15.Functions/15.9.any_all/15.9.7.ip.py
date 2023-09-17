print(all(map(lambda x: str(x).isdigit() and 0 <= int(x) <= 255, input().split('.'))))
