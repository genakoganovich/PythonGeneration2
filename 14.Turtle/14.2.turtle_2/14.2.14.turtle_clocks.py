import turtle

full, turns = (360, 12)


def ray(side, end):
    turtle.penup()
    turtle.forward(side)
    turtle.pendown()
    turtle.forward(end)

    turtle.stamp()
    turtle.back(end)
    turtle.penup()
    turtle.back(side)


def star_rays(side, end):
    turtle.shape('turtle')
    for _ in range(turns):
        ray(side, end)
        turtle.right(full / turns)


if __name__ == '__main__':
    turtle.Screen().bgcolor('gray')
    star_rays(100, 20)
    input()
