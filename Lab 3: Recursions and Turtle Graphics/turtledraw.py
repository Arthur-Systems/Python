#
# DRAW SHAPES
#
import turtle
import tkinter

# draw a circle


def draw_circle(t, size):
    t.pendown()
    t.begin_fill()
    t.circle(size)
    t.end_fill()

# draw a triangle


def draw_triangle(t, size):
    t.pendown()
    t.begin_fill()
    t.fd(size)
    t.lt(120)
    t.fd(size)
    t.lt(120)
    t.fd(size)
    t.end_fill()

# draw a rectangle


def draw_rectangle(t, width, height):
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()

# draw a star


def draw_star(t, size):
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()

# draw spiral


def draw_spiral(t, size, factor, angle):
    t.pendown()
    for x in range(size):
        t.fd(factor*x)
        t.left(angle)


# main program
s = turtle.Screen()     # make a canvas window
s.setup(400, 400)
s.bgcolor("ivory4")
s.title("Turtle Program")

t = turtle.Turtle()     # make a pen
t.shape("turtle")
t.pen(pencolor='dark violet', fillcolor='dark violet', pensize=1, speed=0)

t.penup()
t.goto(-150, 100)        # move the pen to the left upper corner
draw_circle(t, 20)

t.penup()
t.goto(100, -100)        # move the pen to the right bottom corner
t.color('gold')
draw_rectangle(t, 50, 70)

t.penup()
t.goto(-150, -100)       # move the pen to the left bottom corner
t.color('aqua')
draw_triangle(t, 50)

t.penup()
t.goto(120, 150)         # move the pen to the right upper corner
t.color('red')
draw_star(t, 50)

t.penup()
t.home()                # move the pen to the center
t.color('coral')
draw_spiral(t, 80, 2, 92)

t.penup()
t.home()

s.exitonclick()
