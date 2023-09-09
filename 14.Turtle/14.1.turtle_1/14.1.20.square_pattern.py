import turtle

turns, full = (4, 360)


def polygon(side):
    for _ in range(turns):
        turtle.back(side)
        turtle.right(full / turns)


def square_pattern(side, size):
    for i in range(size):
        polygon(side * (1 + i / size))


if __name__ == '__main__':
    square_pattern(100, 10)
    input()
