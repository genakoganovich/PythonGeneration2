import turtle
import time

turns, full, length = (3, 360, 60)


def polygon_down(side):
    for _ in range(turns):
        turtle.forward(side)
        turtle.right(full / turns)


def polygon_up(side):
    for _ in range(turns):
        turtle.left(full / turns)
        turtle.forward(side)


if __name__ == '__main__':
    polygon_up(length)
    turtle.goto(0, 0)
    time.sleep(4)
    turtle.penup()
    turtle.goto(turtle.xcor() - length, turtle.ycor() + length // 2)
    turtle.pendown()
    polygon_down(length)
    input()
