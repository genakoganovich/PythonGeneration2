import turtle
import time

radius = 100


def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(r)


def bear():
    draw_circle(0, 0, radius)
    draw_circle(0, 0, radius // 2)
    turtle.penup()
    turtle.goto(0, radius // 4)
    turtle.pendown()
    turtle.goto(0, 2 * radius // 3)
    draw_circle(turtle.xcor(), turtle.ycor(), radius // 8)
    draw_circle(radius // 2, radius, radius // 8)
    draw_circle(-radius // 2, radius, radius // 8)
    draw_circle(-3 * radius // 4, 14 * radius // 8, radius // 4)
    draw_circle(3 * radius // 4, 14 * radius // 8, radius // 4)


if __name__ == '__main__':
    bear()
    turtle.hideturtle()
    input()
