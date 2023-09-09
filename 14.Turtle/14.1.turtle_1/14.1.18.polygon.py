import turtle

turns, full = (3, 360)


def polygon(side):
    for _ in range(turns):
        turtle.forward(side)
        turtle.right(full / turns)


if __name__ == '__main__':
    polygon(60)
    input()
