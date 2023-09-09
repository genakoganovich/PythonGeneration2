import turtle
import time


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)


def honeycomb(side):
    for _ in range(6):
        turtle.left(120)
        turtle.forward(side)
        turtle.right(60)
        hexagon(side)


if __name__ == '__main__':
    honeycomb(100)
    input()
