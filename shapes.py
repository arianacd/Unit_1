import turtle
turtle.speed(0)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.forward(100)
turtle.pendown()
for x in range(5):
    turtle.forward(90)
    turtle.left(72)
turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.circle(50)
turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.pendown()
for x in range(5):
    turtle.forward(50)
    turtle.left(144)
turtle.right(45)
turtle.penup()
turtle.forward(80)
turtle.pendown()
for x in range(4):
    turtle.forward(80)
    turtle.left(90)
turtle.right(20)
for x in range(4):
    turtle.forward(80)
    turtle.left(90)
turtle.right(20)
for x in range(4):
    turtle.forward(80)
    turtle.left(90)
turtle.right(20)
turtle.seth(0)
turtle.penup()
turtle.fd(100)
turtle.down()

def make_a_house():
    turtle.color("red")
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(80)
        turtle.left(120)
    turtle.end_fill
    turtle.lf(60)
    turtle.color("blue")
    turtle.begin_fill()
    for x in range(4):
        turtle.fd(80)
        turtle.left(90)
    turtle.end_color()


make_a_house()


turtle.exitonclick()

