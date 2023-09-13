import turtle

turtle.hideturtle()
turtle.goto(-120, 120)
turtle.write('Сверху', move=True, align='center', font=('Arial', 17, 'bold'))
turtle.goto(50, -120)
turtle.write('Снизу', move=True, align='left', font=('Times New Roman', 25, 'normal'))
turtle.goto(100, 20)
turtle.write('Справа', move=True, align='right', font=('Helvetica', 20, 'italic'))
input()
