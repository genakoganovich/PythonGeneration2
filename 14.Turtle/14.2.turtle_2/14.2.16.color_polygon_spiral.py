import turtle

length, size, delta, pen_size, wid_delta, turn, full = (10, 20, 5, 5, 1, 8, 360)
colors = ['green', 'purple', 'orange', 'red', 'blue', 'yellow']


def polygon_spiral():
    for i in range(size):
        turtle.pensize(pen_size + i * wid_delta)
        turtle.pencolor(colors[i % len(colors)])
        turtle.back(length + i * delta)
        turtle.left(full / turn)


if __name__ == '__main__':
    polygon_spiral()
    input()
