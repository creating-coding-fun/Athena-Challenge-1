import turtle

pen = turtle.Turtle()
def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

def heart(color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(114)
    curve()
    turtle.left(120)
    curve()
    turtle.forward(115)
    turtle.end_fill()

def flash_heart(color1, color2):
    heart(color1)
    turtle.update()
    turtle.ontimer(lambda:flash_heart(color2,color1), 100)
    turtle.update()
    pen.clear()



screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(500, 450)
turtle.speed(0)
turtle.pencolor('red')

flash_heart('pink', 'red')

screen.mainloop()









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
