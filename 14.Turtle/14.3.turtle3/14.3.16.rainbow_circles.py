import turtle
from random import randrange

turtle.Screen().colormode(255)
radius = 100

for i in range(10):
    turtle.dot(radius - i * 8, (randrange(256), randrange(256), randrange(256)))

input()
