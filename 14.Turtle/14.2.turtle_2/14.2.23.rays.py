import turtle

height, width, size = (100, 150, 10)


def one_ray(length, angle):
    pass


def rays():
    for i in range(size):
        turtle.pencolor('cyan')
        turtle.goto(width - 2 * i * width // size, -height)
        turtle.dot(10, 'blue')
        turtle.pencolor('cyan')
        turtle.goto(0, 0)

    turtle.dot(10, 'red')
    turtle.hideturtle()


if __name__ == '__main__':
    rays()
    input()
