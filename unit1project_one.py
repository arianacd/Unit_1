# unit1project_one
# by Ariana Daney
# Last modified September 17, 2019
# This program makes four octagons of different colors in different locations
import turtle

# This function is to make an octagon with a choice of color


def makeanoctagon(color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.fd(50)
        turtle.left(45)
    turtle.end_fill()

# This function is to move the turtle to a choice location


def go_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.down()

# the following lines make octagons of different colors in new locations


makeanoctagon("hot pink")
go_to(-150, 0)
makeanoctagon("turquoise")
go_to(-150, -150)
makeanoctagon("magenta")
go_to(0, -150)
makeanoctagon("cyan")

# This makes the program stay on the screen until its clicked
turtle.exitonclick()
