import turtle

# makes a triangle
turtle.speed(0)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
# turtle moves without being seen
turtle.penup()
turtle.forward(100)
turtle.pendown()
# turtle makes a square
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
# turtle moves without being seen
turtle.penup()
turtle.forward(100)
turtle.pendown()
# turtle makes a pentagon
for x in range(5):
    turtle.forward(90)
    turtle.left(72)
# turtle moves without being seen
turtle.penup()
turtle.forward(200)
turtle.pendown()

turtle.circle(50)
turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.pendown()
# turtle makes a star
for x in range(5):
    turtle.forward(50)
    turtle.left(144)
turtle.right(45)
turtle.penup()
turtle.forward(80)
turtle.pendown()
# turtle makes rotating squares
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
turtle.goto(200,200)
turtle.down()
turtle.left(120)

# function to make a house with different colors
def make_a_house(color, color2):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(80)
        turtle.left(120)
    turtle.end_fill()
    turtle.left(60)
    turtle.color(color2)
    turtle.begin_fill()
    for y in range(4):
        turtle.fd(80)
        turtle.left(90)
    turtle.end_fill()

def go_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.down()


make_a_house("red", "blue")

go_to(-300, -300)
make_a_house("green", "yellow")

turtle.exitonclick()

