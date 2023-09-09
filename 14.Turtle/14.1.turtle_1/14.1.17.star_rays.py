import turtle

turns, full = (12, 360)


def ray(side):
    turtle.forward(side)
    turtle.back(side)


def star_rays(side):
    for _ in range(turns):
        ray(side)
        turtle.right(full / turns)


if __name__ == '__main__':
    star_rays(100)
    input()
