import time
import turtle

turtle.Screen().addshape('rocketship.gif')  # регистрируем изображение
turtle.shape('rocketship.gif')  # устанавливаем изображение

for _ in range(4):
    turtle.forward(150)
    turtle.left(90)

time.sleep(4)
