from math import sin, pi
import turtle


def polygon(size, n):
    t.pendown()
    for i in range(n):
        t.forward(size)
        t.left(360/n)
    t.penup()


def polygon_wrapper(size, n):
    polygon_recursive(size, n, 360/n)


def polygon_recursive(size, n, alpha):
    if n > 0:
        t.pendown()
        t.forward(size)
        t.left(alpha)
        t.penup()
        polygon_recursive(size, n-1, alpha)
    else:
        return


def star(size, n, d=2):
    density = d
    interior_angle = 360*(density-1)/n
    if n % density == 0:    # If even number of sides
        for j in range(density):
            t.pendown()
            for i in range(n // density):
                t.left(interior_angle)
                t.forward(size)
                t.left(interior_angle)
            t.penup()
            t.circle((size) / (2 * sin((pi/(n // density)))), interior_angle)
    else:  # If odd number of sides
        t.pendown()
        for i in range(n):
            t.left(interior_angle)
            t.forward(size)
            t.left(interior_angle)
        t.penup()


def star_wrapper(size, n, d=2):
    star_recursive(size, n, 360*(d-1)/n, d)


def star_recursive(size, n, alpha, d=2):
    if d == 2 and n % d == 0 and n > 5:  # if the number of sides is less then the minium number to make a star this condition will be false
        star_recursive(size, n//d, alpha, d=0)
        t.circle((size) / (2 * sin((pi/(n // d)))), alpha)
        star_recursive(size, n//d, alpha, d=0)
    else:
        if n > 0:
            t.pendown()
            t.left(alpha)
            t.forward(size)
            t.left(alpha)
            t.penup()
            star_recursive(size, n-1, alpha, d + 1)


if __name__ == "__main__":
    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Turtle Program")

    t = turtle.Turtle()
    t.shape("turtle")
    t.pen(speed=5)

    t.penup()
    t.goto(-200, 100)
    polygon(100, 7)

    t.goto(200, 100)
    polygon_wrapper(100, 7)

    t.goto(-200, -150)
    star(100, 12)  # function works with odd AND even numbers

    t.goto(-200, -250)
    t.left(180)
    star(100, 5)  # function works with odd AND even numbers

    t.goto(200, -100)
    t.right(180)
    star_wrapper(100, 12)   # function works with odd AND even numbers

    t.goto(200, -250)
    t.left(90)
    star_wrapper(100, 5)   # function works with odd AND even numbers

    turtle.done()
