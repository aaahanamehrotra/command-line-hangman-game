import turtle
turtle.hideturtle()
def make_head():
    turtle.penup()
    turtle.setpos(0,0)
    turtle.pendown()
    i = 360
    while i >= 0:
        turtle.speed(500)
        turtle.forward(1)
        turtle.left(1)
        i -= 1
def make_body():
    turtle.penup()
    turtle.setpos(0,0)
    turtle.pendown()
    turtle.goto(0,-150)
def make_rhand():
    turtle.penup()
    turtle.setpos(0,-100)
    turtle.pendown()
    turtle.goto(100,0)
def make_lhand():
    turtle.penup()
    turtle.setpos(0,-100)
    turtle.pendown()
    turtle.goto(-100,0)
def make_rleg():
    turtle.penup()
    turtle.setpos(0,-150)
    turtle.pendown()
    turtle.goto(100,-250)
def make_lleg():
    turtle.penup()
    turtle.setpos(0,-150)
    turtle.pendown()
    turtle.goto(-100,-250)
