import turtle
import time


def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)


def draw(side):
    turtle.left(90)
    for _ in range(8):
        turtle.left(45)
        square(side)


if __name__ == '__main__':
    draw(100)
    time.sleep(4)
