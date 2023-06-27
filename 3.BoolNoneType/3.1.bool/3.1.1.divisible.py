def func(num1, num2):
    return not num1 % num2


def run(num1, num2):
    print('делится' if func(num1, num2) else 'не делится')


run(int(input()), int(input()))
