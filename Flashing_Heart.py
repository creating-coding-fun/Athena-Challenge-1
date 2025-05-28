import turtle


screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(500, 450)
screen.tracer(0)

pen = turtle.Turtle()
pen.shape("turtle")
turtle.pencolor('red')
pen.speed(0)

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart(color):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.left(140)
    pen.forward(114)
    curve()
    pen.left(120)
    curve()
    pen.forward(115)
    pen.end_fill()
    screen.update()

def flash_heart(color1, color2, color3,  current_color=1):
    if current_color == 1:
        heart(color1)
        current_color = 2

    elif current_color == 2:
        heart(color2)
        current_color = 3

    else:
        heart(color3)
        current_color = 1

    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()
    pen.hideturtle()
    turtle.hideturtle()
    screen.ontimer(lambda: flash_heart(color1, color2, color3,  current_color), 350)


screen.update()
flash_heart("pink", "red", "magenta")



screen.mainloop()









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
