import turtle


def SetTurtle():
    s = turtle.Screen()
    s.bgcolor("white")
    s.setup(1000, 1000)
    s.title("Tree Program")
    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)
    t.speed(0)
    return t, s


def DrawTree(t, size, width):
    if size > 0:
        t.color("#765c48")
        t.pensize(width)
        t.pendown()
        t.forward(size)
        t.left(20)
        DrawTree(t, size - 10, width - 1)
        t.right(40)
        DrawTree(t, size - 10, width - 1)
        t.left(20)
        t.penup()
        t.backward(size)
    else:
        t.color("#00ff00")
        t.dot(12)


if __name__ == "__main__":
    t, s = SetTurtle()
    t.left(90)
    turtle.tracer(15)
    t.penup()
    t.goto(0, -400)
    t.pendown()
    DrawTree(t, 100, 10)

    turtle.update()
    turtle.done()
