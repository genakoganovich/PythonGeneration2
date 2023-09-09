import turtle

turns, full = (5, 360)


def star_5(side):
    for _ in range(turns):
        turtle.right(2 * full / turns)
        turtle.forward(side)


if __name__ == '__main__':
    star_5(100)
    input()
