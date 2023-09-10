import turtle

turtle.shape('circle')


def rectangle(width, height):
    for _ in range(4):
        turtle.forward(width)
        turtle.stamp()
        turtle.right(90)
        width, height = height, width


rectangle(200, 100)
input()
