import turtle
import time


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)


if __name__ == '__main__':
    hexagon(100)
    time.sleep(4)
