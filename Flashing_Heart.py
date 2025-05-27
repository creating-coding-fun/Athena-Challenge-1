import turtle


screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(500, 450)

pen = turtle.Turtle()
pen.shape("turtle")
turtle.pencolor('red')
pen.speed(0)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

def heart():
    turtle.fillcolor('pink')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(114)
    curve()
    turtle.left(120)
    curve()
    turtle.forward(115)
    turtle.end_fill()
    turtle.done()

def flash_heart(color1, color2):
    pen.clear()
    pen.penup()
    pen.position()
    pen.setheading(0)
    heart()
    screen.update()
    screen.ontimer(lambda: flash_heart(color1, color2), 500)



flash_heart('pink', 'red')
heart()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
