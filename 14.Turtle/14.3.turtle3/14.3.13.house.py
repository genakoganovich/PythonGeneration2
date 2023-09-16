import turtle

full, length = (360, 100)


def polygon_up(side, turns):
    for _ in range(turns):
        turtle.forward(side)
        turtle.left(full / turns)


def polygon_down(side, turns):
    for _ in range(turns):
        turtle.forward(side)
        turtle.right(full / turns)


if __name__ == '__main__':
    turtle.fillcolor('red')
    turtle.begin_fill()
    polygon_up(length, 3)
    turtle.end_fill()
    turtle.fillcolor('green')
    turtle.begin_fill()
    polygon_down(length, 4)
    turtle.end_fill()
    input()
