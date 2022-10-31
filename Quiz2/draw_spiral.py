import turtle

# draw a spiral


def draw_spiral(t, segments, size, angle):
    t.pendown()
    if segments == 0:
        return
    else:
        t.fd(size)
        t.left(angle)
        draw_spiral(t, segments - 1, size + 2, angle)


# driver code
if __name__ == '__main__':
    s = turtle.Screen()
    s.setup(400, 400)
    t = turtle.Turtle()
    t.pen(pencolor='dark violet', pensize=2, speed=0)
    t.penup()
    t.home()
    draw_spiral(t, 160, 2, 92)
    turtle.done()
