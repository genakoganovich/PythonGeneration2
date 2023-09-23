n = int(input())
for _ in range(n):
    with open(input()) as file_in, open('output.txt', 'a') as file_out:
        file_out.write(file_in.read())
