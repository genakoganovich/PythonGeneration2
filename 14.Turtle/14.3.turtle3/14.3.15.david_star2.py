import turtle
import time

turns, full, length = (3, 360, 60)


def polygon_down(side):
    turtle.penup()
    turtle.color('white')
    turtle.begin_fill()
    for _ in range(turns):
        turtle.forward(side)
        turtle.right(full / turns)
    turtle.end_fill()


def circles(side):
    turtle.penup()
    for _ in range(turns):
        turtle.forward(side)
        turtle.dot(30, 'black')
        turtle.right(full / turns)


def polygon_up(side):
    for _ in range(turns):
        turtle.left(full / turns)
        turtle.forward(side)


if __name__ == '__main__':
    polygon_up(length)
    turtle.goto(0, 0)
    turtle.penup()
    turtle.goto(turtle.xcor() - length, turtle.ycor() + length // 2)
    turtle.pendown()
    circles(length)
    polygon_down(length)
    input()
