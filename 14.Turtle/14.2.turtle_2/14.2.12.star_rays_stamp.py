import turtle

full, *_ = (360, )


def ray(side):
    turtle.forward(side)
    turtle.stamp()
    turtle.back(side)


def star_rays(side, turns):
    turtle.shape('circle')
    turtle.stamp()
    turtle.shape('triangle')
    for _ in range(turns):
        ray(side)
        turtle.right(full / turns)


if __name__ == '__main__':
    n = int(input())
    star_rays(100, n)
    input()
