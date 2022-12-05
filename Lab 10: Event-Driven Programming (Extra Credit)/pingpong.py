# rebounding ball
from tkinter import *


def animation():
    global canvas
    global rect
    global dx
    global dy
    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))

    x1, y1, x2, y2 = canvas.coords(ball)
    if x2 > width or x1 < 0:
        dx = - dx
    if y2 > height or y1 < 0:
        dy = - dy
    canvas.move(ball, dx, dy)
    canvas.after(10, animation)


def checkcollision():
    global canvas
    global paddle
    global ball
    global dx
    global dy
    x1, y1, x2, y2 = canvas.coords(ball)
    x3, y3, x4, y4 = canvas.coords(paddle)
    if x2 > x3 and x1 < x4 and y2 > y3 and y1 < y4:
        dx = -dx
    canvas.after(10, checkcollision)


def move_paddle(event):
    global paddle
    global canvas
    global dx
    global dy
    x1, y1, x2, y2 = canvas.coords(paddle)
    height = int(canvas.cget('height'))
    if event.keysym == 'Up':
        print('Up')
        if y1 > 0:
            canvas.move(paddle, 0, -10)
    elif event.keysym == 'Down':
        if y2 < height:
            canvas.move(paddle, 0, 10)


# main program
gui = Tk()
canvas = Canvas(gui, width=400, height=300, bg='white')
ball = canvas.create_oval(100, 100, 125, 125, fill="red")
paddle = canvas.create_rectangle(100, 250, 125, 125, fill="blue")

canvas.move(paddle, 250, 0)
# paddle2 = canvas.create_rectangle(100, 250, 125, 125, fill="red")
canvas.pack()
dx, dy = 1, 1
animation()
checkcollision()
gui.bind('<Key>', move_paddle)
mainloop()
