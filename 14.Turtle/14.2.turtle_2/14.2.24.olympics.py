import turtle

radius, width = (50, 5)
c_colors = ['black', 'cyan', 'red', 'yellow', 'chartreuse']
c_coord = [(0, 0),
           (-2 * radius - 2 * width, 0),
           (2 * radius + 2 * width, 0),
           (-radius - width, -radius - width),
           (radius + width, -radius - width)]


def draw_circle(x, y, r, w, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(r)


def olympics():
    turtle.pensize(width)
    for i in range(len(c_colors)):
        draw_circle(c_coord[i][0], c_coord[i][1], radius, width, c_colors[i])


if __name__ == '__main__':
    olympics()
    turtle.hideturtle()
    input()
