import turtle


def rectangle(width, height):
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)
        width, height = height, width


rectangle(200, 100)
