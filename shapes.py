import turtle
import random

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

# function to make a house with different colors
def make_a_house(color, color2, size):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
    turtle.left(60)
    turtle.color(color2)
    turtle.begin_fill()
    for y in range(4):
        turtle.fd(size)
        turtle.left(90)
    turtle.end_fill()
    turtle.seth(0)

def go_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.down()


make_a_house("red", "blue", 5)

go_to(-300, -300)

make_a_house("green", "yellow", random.randint(5, 300))

go_to(300, -300)
make_a_house("cyan", "magenta", random.randint(5, 300))
go_to(150, -100)
make_a_house("turquoise", "light green", random.randint(5, 300))
go_to(250, -100)
make_a_house("violet", "sky blue", random.randint(5, 300))
go_to(350, -100)
make_a_house("forest green", "pink", random.randint(5, 300))
turtle.exitonclick()

