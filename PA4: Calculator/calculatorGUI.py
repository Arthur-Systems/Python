# author: Arthur Wei
# date: November 14, 2022
# file: calculatorGUI.py a python file that creates a calculator GUI
# input: Physical Data button clicks from the user
# output: calulated data from shown on the calculator

from tkinter import *
from calculator import calculate


def calculator(gui):  # creates the calculator GUI
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=20, borderwidth=0, font=('Helvetica', 50))
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4,
                  padx=10, pady=10, ipady=10, ipadx=10)

    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=
    b0 = addButton(gui, entrybox, '0')
    b1 = addButton(gui, entrybox, '1')
    b2 = addButton(gui, entrybox, '2')
    b3 = addButton(gui, entrybox, '3')
    b4 = addButton(gui, entrybox, '4')
    b5 = addButton(gui, entrybox, '5')
    b6 = addButton(gui, entrybox, '6')
    b7 = addButton(gui, entrybox, '7')
    b8 = addButton(gui, entrybox, '8')
    b9 = addButton(gui, entrybox, '9')
    b_add = addButton(gui, entrybox, '+')
    b_sub = addButton(gui, entrybox, '-')
    b_mult = addButton(gui, entrybox, '*')
    b_div = addButton(gui, entrybox, '/')
    b_clr = addButton(gui, entrybox, 'c')
    b_eq = addButton(gui, entrybox, '=')

    # add buttons to the grid
    buttons = [b7,    b8, b9,    b_clr,
               b4,    b5, b6,    b_sub,
               b1,    b2, b3,    b_add,
               b_mult, b0, b_div, b_eq]
    k = 4
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)
    gui.bind('<Return>', lambda event: clickButton(
        entrybox, '='))  # Keyboard listeners
    gui.bind('<BackSpace>', lambda event: clickButton(entrybox, 'c'))
    gui.bind('<Key>', lambda event: clickButton(
        entrybox, event.char if event.char in '0123456789+-*/^' else ''))


def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=6, width=8, command=lambda: clickButton(entrybox, value), font=('Helvetica', 30), borderwidth=0)


def clickButton(entrybox, value):
    if value == 'c':
        entrybox.delete(0, END)
    elif value == '=':
        if entrybox.get() != '':
            value = calculate(entrybox.get())
            entrybox.delete(0, END)
            entrybox.insert(0, value)

    else:
        entrybox.insert(END, value)


# main program
# create the main window
gui = Tk()

# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()
