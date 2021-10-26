###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
from turtle import Turtle, Screen
import colorgram

rgb_colors = []
colors = colorgram.extract('hirst-spot-painting.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

slash = Turtle()
screen = Screen()

screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
screen.colormode(255)

slash.penup()
slash.hideturtle()
slash.speed("fastest")

for i in range(1,11):
    for _ in range(10):
        slash.color(random.choice(rgb_colors))
        slash.dot(20)
        slash.forward(50)
    slash.setx(0)
    slash.sety(50 * i)

screen.exitonclick()