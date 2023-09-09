import turtle


def rhombus(side):
    turtle.forward(side)
    for i in [60, 120, 60]:
        turtle.right(i)
        turtle.forward(side)


if __name__ == '__main__':
    rhombus(100)
    input()