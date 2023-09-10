import turtle
import random

turns, full, width, size = (8, 360, 400, 10)


def flake(side):
    turtle.back(side)
    turtle.left(45)
    turtle.forward(side)
    turtle.back(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.back(side)
    turtle.left(45)


def ray(side):
    turtle.forward(side)
    for _ in range(3):
        flake(side // 4)

    turtle.back(side // 4)


def snow(side, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(turns):
        ray(side)
        turtle.right(full / turns)


if __name__ == '__main__':
    turtle.Screen().setup(width, width)
    turtle.bgcolor('cyan')
    for _ in range(size):
        snow(random.randint(10, 20), random.randint(-width // 2, width // 2), random.randint(-width // 2, width // 2))
    turtle.hideturtle()
    input()
