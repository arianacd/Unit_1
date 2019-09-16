# unit1project_one
# by Ariana Daney
# Last modified September 16, 2019
#
# This program makes four octagons of different colors
import turtle

# function to make an octagon


def makeanoctagon():
    for x in range(8):
        turtle.fd(50)
        turtle.left(45)

# function to change turtle's location


def go_to(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.down()

# makes a hot pink octagon


turtle.color("hot pink")
turtle.begin_fill()
makeanoctagon()
turtle.end_fill()
# makes a turquoise octagon in a new location
go_to(-150,0)
turtle.color("turquoise")
turtle.begin_fill()
makeanoctagon()
turtle.end_fill()
# makes a magenta octagon in a new location
go_to(-150,-150)
turtle.color("magenta")
turtle.begin_fill()
makeanoctagon()
turtle.end_fill()
# makes a cyan octagon in a new location
go_to(0,-150)
turtle.color("cyan")
turtle.begin_fill()
makeanoctagon()
turtle.end_fill()
# the program stays on the screen until its clicked
turtle.exitonclick()