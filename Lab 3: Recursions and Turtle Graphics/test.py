"""
koch.py

Description:

A program that explores the Koch snowflake and the Thue-Morse sequence.

Author: Mahesh Venkitachalam
Website: electronut.in
"""

import time
import turtle
import math
import sys
import argparse

# generate the Thue-Morse sequence


def genThueMorse():
    # initialize
    tms = '0'
    curr = 0
    while True:
        # generate next sequence
        if curr == len(tms):
            tmp = ''
            for i in range(len(tms)):
                if tms[i] is '0':
                    tmp += '1'
                else:
                    tmp += '0'
            tms += tmp
        yield tms[curr]
        curr += 1

# turtle graphics using Thue-Morse sequence


def drawTM(x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    t.setpos(x, y)
    t.down()
    tms = genThueMorse()
    delta = 4
    while True:
        a = next(tms)
        if a is '0':
            t.fd(delta)
        else:
            t.left(60)

# recursive koch snow flake


def kochSF(x1, y1, x2, y2, t):
    d = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    r = d/3.0
    h = r*math.sqrt(3)/2.0
    p3 = ((x1 + 2*x2)/3.0, (y1 + 2*y2)/3.0)
    p1 = ((2*x1 + x2)/3.0, (2*y1 + y2)/3.0)
    c = (0.5*(x1+x2), 0.5*(y1+y2))
    n = ((y1-y2)/d, (x2-x1)/d)
    p2 = (c[0]+h*n[0], c[1]+h*n[1])
    if d > 10:
        # flake #1
        kochSF(x1, y1, p1[0], p1[1], t)
        # flake #2
        kochSF(p1[0], p1[1], p2[0], p2[1], t)
        # flake #3
        kochSF(p2[0], p2[1], p3[0], p3[1], t)
        # flake #4
        kochSF(p3[0], p3[1], x2, y2, t)
    else:
        # draw cone
        t.up()
        t.setpos(p1[0], p1[1])
        t.down()
        t.setpos(p2[0], p2[1])
        t.setpos(p3[0], p3[1])
        # draw sides
        t.up()
        t.setpos(x1, y1)
        t.down()
        t.setpos(p1[0], p1[1])
        t.up()
        t.setpos(p3[0], p3[1])
        t.down()
        t.setpos(x2, y2)

# draw a koch snowflake


def drawKochSF(x1, y1, x2, y2):
    t = turtle.Turtle()
    t.hideturtle()
    kochSF(x1, y1, x2, y2, t)

# main() function


def main():
    print('Exploring the Koch Snowflake...')

    parser = argparse.ArgumentParser(description="Koch Snowflake")
    # add arguments
    parser.add_argument('--thue', action='store_true', required=False)
    args = parser.parse_args()

    if args.thue:
        drawTM(200, 200)
    else:
        drawKochSF(-100, 0, 100, 0)
        drawKochSF(0, -173.2, -100, 0)
        drawKochSF(100, 0, 0, -173.2)
        win = turtle.Screen()
        win.exitonclick()


# call main
if __name__ == '__main__':
    main()
