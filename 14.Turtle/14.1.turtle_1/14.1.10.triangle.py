import turtle
import time


def triangle(side):
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)


if __name__ == '__main__':
    triangle(100)
    time.sleep(4)
