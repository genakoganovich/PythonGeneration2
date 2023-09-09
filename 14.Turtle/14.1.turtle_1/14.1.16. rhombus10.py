import turtle

turns, full = (10, 360)


def rhombus(side):
    for i in [0, 60, 120, 60]:
        turtle.right(i)
        turtle.forward(side)


def rhombus_10(side):
    for _ in range(turns):
        rhombus(side)
        turtle.right(120 + full / turns)


if __name__ == '__main__':
    rhombus_10(100)
    input()
