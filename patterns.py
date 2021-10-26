from turtle import Turtle, Screen
import random

turt = Turtle()
screen = Screen()

turt.shape("turtle")
screen.colormode(255);

def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)


############################################################
# 1) Draws shapes from triangle to decagon
############################################################


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        rgb = random_rgb()
        turt.pencolorr(rgb)
        turt.forward(100)
        turt.right(angle)

# for sides in range(3, 100):
#     draw_shape(sides)


############################################################
# 2) Turtle Random Walk
############################################################

def left():
    turt.left(90)
    turt.forward(20)

def right():
    turt.right(90)
    turt.forward(20)

def forward():
    turt.forward(20)

def backward():
    turt.backward(20)

directions = [left, right, forward, backward]
# turt.pensize(15)

# for _ in range(100):
#     rgb = random_rgb()
#     turt.pencolor(rgb)
#     random.choice(directions)()


############################################################
# 3) Draw a spirograph
############################################################

# turt.speed("fastest")
#
# tilt = 10
# for i in range(450):
#     rgb = random_rgb()
#     turt.pencolor(rgb)
#
#     turt.circle(100)
#     turt.right(tilt)
#     if i % 100 == 0:
#         tilt -= 2



screen.exitonclick()
