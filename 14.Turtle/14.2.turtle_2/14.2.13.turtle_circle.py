import turtle

full, turns = (360, 10)


def ray(side):
    turtle.forward(side)
    turtle.stamp()
    turtle.back(side)


def star_rays(side):
    turtle.penup()
    turtle.shape('turtle')
    turtle.stamp()

    for _ in range(turns):
        ray(side)
        turtle.right(full / turns)


if __name__ == '__main__':
    star_rays(100)
    input()
