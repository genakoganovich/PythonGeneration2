import turtle
from random import randrange

turtle.Screen().colormode(255)


def move_turtles(turtle_list, dist, angle):
    for t in turtle_list:  # все черепашки из списка делают одни и те же действия
        t.forward(dist)
        t.right(angle)


turtles = []  # список черепашек
head = 0
num_turtles = 10  # количество череашек
for i in range(num_turtles):
    turt = turtle.Turtle()  # создаем черепашку и устанавливаем ее свойства
    turt.setheading(head)
    turt.pensize(2)
    turt.color(randrange(256), randrange(256), randrange(256))
    turt.speed(5)
    # turt.tracer(25, 0)
    turtle.tracer(25, 0)
    turtles.append(turt)  # добавляем черепашку в список
    head = head + 360 / num_turtles

for i in range(70):
    move_turtles(turtles, 10, i)

input()
