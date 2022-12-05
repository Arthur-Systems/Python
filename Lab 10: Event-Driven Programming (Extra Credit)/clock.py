# an analog clock
from tkinter import *
import math
from datetime import datetime


def draw_clock():
    canvas.delete("all")
    w, h = 300, 300  # size of the canvas
    x, y = w/2, h/2  # center of the canvas and the clock
    size = 200       # size of the clock
    circle1 = canvas.create_oval(x-size/2, y-size/2,
                                 x+size/2, y+size/2,
                                 fill='ivory')
    circle2 = canvas.create_oval(x-size/2, y-size/2,
                                 x+size/2, y+size/2,
                                 width=3, outline='black')
    ticks1, numbers = [], []
    n = 12
    for i in range(n):
        angle = 2*math.pi*i/n
        ticks1.append(canvas.create_line(x+100*math.cos(angle),
                                         y+100*math.sin(angle),
                                         x+90*math.cos(angle),
                                         y+90*math.sin(angle),
                                         fill='black', width=2))
        numbers.append(canvas.create_text(x+80*math.cos(angle),
                                          y+80*math.sin(angle), text=str((i+2) % n+1)))
    ticks2 = []
    n = 60
    for i in range(n):
        angle = 2*math.pi*i/n
        ticks1.append(canvas.create_line(x+100*math.cos(angle),
                                         y+100*math.sin(angle),
                                         x+95*math.cos(angle),
                                         y+95*math.sin(angle),
                                         fill='black', width=1))
    global time
    time += 1     # add a time interval = 1 sec
    alpha = - math.pi/2 + 2*math.pi * (time % 60) / 60
    arrow1 = canvas.create_line(x, y, x+90*math.cos(alpha), y+90*math.sin(alpha),
                                fill='red', width=2, arrow='last')
    alpha = - math.pi/2 + 2*math.pi * (time % 3600) / 3600
    arrow2 = canvas.create_line(x, y, x+70*math.cos(alpha), y+70*math.sin(alpha),
                                fill='black', width=3, arrow='last')
    alpha = - math.pi/2 + 2*math.pi * (time % 43200) / 43200
    arrow3 = canvas.create_line(x, y, x+50*math.cos(alpha), y+50*math.sin(alpha),
                                fill='black', width=4, arrow='last')
    gui.after(1000, lambda: draw_clock())  # update after 1000 msecs = 1 sec


# main program
gui = Tk()
canvas = Canvas(gui, height=300, width=300)
canvas.pack()
now = datetime.now()
hourtwelve = now.hour % 12
time = now.second + 60*now.minute + 3600*hourtwelve
print(now.second, now.minute, hourtwelve)
draw_clock()
gui.mainloop()
