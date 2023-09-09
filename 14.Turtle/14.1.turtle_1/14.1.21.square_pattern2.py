import turtle

turns, full, delta = (4, 360, 0.1)


def square_pattern(side, size):
    dx = delta
    for i in range(size):
        for j in range(turns):
            turtle.forward(side * (1 + dx))
            dx += delta
            turtle.left(full / turns)


if __name__ == '__main__':
    square_pattern(20, 10)
    input()
