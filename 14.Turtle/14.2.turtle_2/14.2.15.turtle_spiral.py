import turtle

radius, size, delta_radius, delta_angle = (20, 20, 4, 30)


def turtle_spiral():
    turtle.shape('turtle')
    turtle.penup()
    for i in range(size):
        turtle.right(delta_angle)
        turtle.forward(radius + delta_radius * i)
        turtle.right(90)
        turtle.stamp()
        turtle.left(90)
        turtle.back(radius + delta_radius * i)


if __name__ == '__main__':
    turtle.Screen().bgcolor('green')
    turtle_spiral()
    input()
