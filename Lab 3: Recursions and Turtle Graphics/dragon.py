import turtle


def SetTurtle():
    c = turtle.Screen()
    c.bgcolor("white")
    c.setup(1000, 1000)
    c.title("Dragon Program")
    t = turtle.Turtle()
    t.color("black")
    t.pensize(3)
    t.speed(0)
    return t, c


def DrawDragon(n, angle=90):
    if n <= 0:
        t.forward(5)
    else:
        DrawDragon(n - 1, 90)
        t.right(angle)
        DrawDragon(n - 1, -90)


if __name__ == "__main__":
    x = 0
    t, c = SetTurtle()
    turtle.tracer(200)
    t.penup()
    t.goto(-200, 300)
    t.pendown()
    t.left(180)
    DrawDragon(14)
    turtle.update()
    turtle.done()
