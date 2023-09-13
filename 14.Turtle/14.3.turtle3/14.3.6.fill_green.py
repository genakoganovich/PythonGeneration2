import turtle

turtle.hideturtle()
turtle.fillcolor('green')

turtle.begin_fill()

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()
input()
