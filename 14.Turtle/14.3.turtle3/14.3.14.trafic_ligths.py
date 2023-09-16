import turtle

w, h = (80, 180)


def rectangle(width, height):
    for _ in range(4):
        turtle.forward(width)
        turtle.right(90)
        width, height = height, width


if __name__ == '__main__':
    turtle.begin_fill()
    rectangle(w, h)
    turtle.end_fill()
    x, y = turtle.pos()
    turtle.goto(x + w // 2, y)
    turtle.color('white')

    for _ in range(3):
        x, y = turtle.pos()
        turtle.goto(x, y - h // 4)
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
    input()
