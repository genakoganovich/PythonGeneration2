import turtle

turtle.Screen().colormode(255)

turtle.pencolor('red')  # строковое представление цвета
turtle.circle(90)

color = (13, 56, 240)  # кортеж (r, g, b)

turtle.pencolor(color)  # кортеж в качестве аргумента
turtle.circle(80)

turtle.pencolor(130, 240, 200)  # значения r, g, b в качестве аргументов
turtle.circle(50)
input()
