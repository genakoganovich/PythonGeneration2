
import turtle

turtle.Screen().setup(400, 400)               # устанавливаем размер граф. окна
turtle.Screen().addshape('rocketship.gif')    # добавляем форму черепашки

turtle.Screen().bgpic('nerd.png')            # устанавливаем фоновое изображение
turtle.shape('rocketship.gif')                # устанавливаем форму черепашки
turtle.pencolor('green')
turtle.pensize(5)

for _ in range(4):
  turtle.forward(150)
  turtle.left(90)

input()