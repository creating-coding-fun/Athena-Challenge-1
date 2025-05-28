import turtle



screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(500, 450)
screen.tracer(0)
screen.title("I LOVE YOU!!! <3")

pen = turtle.Turtle()
pen.shape("turtle")
turtle.pencolor('red')
pen.speed(0)

text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.goto(0, -100)

colors = ["red", "yellow", "orange", "magenta", "cyan", "green", "purple", "pink", "blue"]
msg = "  I LOVE YOU!"

charc_width = 30
start_point = -(len(msg) * charc_width)// 2

for i, letter in enumerate(msg):
    text.goto(start_point + i * charc_width, -100)
    text.color(colors[i % len(colors)])
    text.write(letter, align='center', font=('Arial', 26, 'bold'))


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
def turtle_reset():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()
    pen.hideturtle()
    turtle.hideturtle()

def flash_heart(color1, color2, color3, color4, current_color=1):
    turtle_reset()

    if current_color == 1:
        heart(color1)
        current_color = 2
    elif current_color == 2:
        heart(color2)
        current_color = 3
    elif current_color == 3:
        heart(color3)
        current_color = 4
    else:
        heart(color4)
        current_color = 1

    screen.ontimer(lambda: flash_heart(color1, color2, color3, color4,   current_color), 100)



screen.update()
flash_heart("pink", "red", "magenta", "cyan")
flash_heart("blue","gold", "purple", "white" )
flash_heart("pink", "red", "magenta", "cyan")
screen.mainloop()










# See PyCharm help at https://www.jetbrains.com/help/pycharm/
