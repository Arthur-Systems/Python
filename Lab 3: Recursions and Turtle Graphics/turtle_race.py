# turtle race
from turtle import *
from random import randint
import time  # import time module


def set_turtles(colors):
    turtles = []
    for color in colors:
        t = Turtle()
        t.color(color)
        t.shape("turtle")
        t.speed(1)
        turtles.append(t)
    return turtles


def draw_track(start, finish):
    t = Turtle()
    t.speed(0)
    position, size, step = 100, 200, 40
    count = 0
    penup()
    hideturtle()
    goto(0, 150)
    write(f"turtle race!".title(),
          align="center", font=("Arial", 20, "bold"))
    for line in range(start, finish + step, step):
        t.penup()
        t.goto(line, position+10)
        if line == start:
            t.color("blue")
            t.pensize(10)
            t.write("START")
        elif line == finish:
            t.color("red")
            t.pensize(10)
            t.write("FINISH")
        else:
            t.color("grey")
            t.pensize(1)
            t.write(count)
        t.goto(line, position)
        count += 1
        t.right(90)
        t.pendown()
        t.forward(size)
        t.left(90)


def isfinish(t, finish):
    x, y = t.pos()
    if x < finish:
        return False
    else:
        return True


def race(turtles, start, finish):
    # y position
    position = 80
    distance = 40
    for t in turtles:
        t.speed(7)  # Speed up the turtles moving
        t.penup()
        t.left(180)
        t.goto(start, position)
        position -= distance
        t.left(180)
        t.pendown()
    done = False
    StartTime = time.time()
    while not done:
        for t in turtles:
            t.forward(randint(1, 10))
            if isfinish(t, finish):
                undo()
                winner(t)
                highlight(t)
                Timer(StartTime)
                button()
                done = True
                break


def winner(t):
    penup()
    hideturtle()
    goto(0, 150)
    write(f"The {t.color()[0]} Turtle won!".title(),
          align="center", font=("Arial", 20, "bold"))


def Timer(StartTime):
    timer = Turtle()
    timer.hideturtle()
    timer.penup()
    timer.goto(-170, -150)
    timer.write(f"Time: {time.time() - StartTime:.2f} seconds",
                align="center", font=("Arial", 15, "bold"))


def highlight(t):  # draw a circle around the winner
    x, y = t.pos()
    goto(x, y-20)
    pendown()
    color(t.color()[0])
    pensize(5)
    speed(8)
    circle(20)
    penup()


def button():  # draw a button to restart the game
    button = Turtle()
    button.hideturtle()
    arrow = Turtle()
    arrow.hideturtle()
    arrow.left(180)
    arrow.penup()
    button.penup()
    button.goto(0, -150)
    button.color("black")
    button.showturtle()
    arrow.color("white")
    button.turtlesize(2, 5)
    button.goto(0, -130)
    button.shape("square")
    button.write("Click Here To Restart The Game!",
                 align="center", font=("Arial", 12, "bold"))
    button.goto(0, -150)
    arrow.goto(-10, -150)
    arrow.showturtle()
    button.onclick(restart)
    arrow.onclick(restart)


def restart(x, y):  # clear the screen
    clear()
    s.clear()
    play()


def play():  # restart the game
    draw_track(start, finish)
    turtles = set_turtles(["yellow", "crimson", "aqua", "green", "purple"])
    race(turtles, start, finish)


if __name__ == "__main__":
    # main program
    s = Screen()     # make a canvas window
    s.setup(500, 400)
    s.bgcolor("white")
    s.title("Turtle Race")
    start = -200  # x position
    finish = 200  # x position
    draw_track(start, finish)
    turtles = set_turtles(["yellow", "crimson", "aqua", "green", "purple"])
    race(turtles, start, finish)
    done()
