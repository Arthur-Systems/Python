import turtle


def snowflake_wrapper(size, depth, n=3):
    if n > 0:
        snowflake(size, depth)
        t.right(120)
        snowflake_wrapper(size, depth, n-1)


def snowflake(size, depth):
    if depth > 0:
        snowflake(size/3, depth-1)
        t.left(60)
        snowflake(size/3, depth-1)
        t.right(120)
        snowflake(size/3, depth-1)
        t.left(60)
        snowflake(size/3, depth-1)
    else:
        t.forward(size)


if __name__ == "__main__":
    t = turtle.Turtle()
    turtle.tracer(25)
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    snowflake_wrapper(500, 5)
    turtle.update()
    turtle.done()
