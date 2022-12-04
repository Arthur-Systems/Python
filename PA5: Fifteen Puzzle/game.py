# author: Arthur Wei
# date: November 14, 2022
# file: game.py a python file that creates a GUI for the fifteen puzzle game
# input: User inputted commands
# output: The game of fifteen with the user's commands

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen


def clickButton(i):
    tiles.update(tiles.tiles[i])  # update the tiles
    Update()


def Update():
    for i in range(16):
        if tiles.tiles[i] == 0:
            buttons[i].config(text=' ', bg='white')
        else:
            buttons[i].config(text=str(tiles.tiles[i]), bg='white')
    if tiles.is_solved():  # if the game is solved
        print('solved!')
        gui.tk_setPalette(background='green')
        for i in range(16):
            buttons[i].config(fg='green')
        text.config(text='Solved!', fg='black')
    else:
        gui.tk_setPalette(background='black')  # set the background to black
        for i in range(16):
            buttons[i].config(fg='black')
        text.config(
            text='Click on a tile to move it. Click shuffle to shuffle the tiles.', fg='white')
        shufflebutton.config(text='Shuffle', fg='black')


def shuffle():  # shuffle the tiles
    tiles.shuffle()
    clickButton(i)


if __name__ == '__main__':

    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    display = Entry(gui)
    display.grid(row=0, column=0, columnspan=4)

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons
    buttons = []
    for i in range(16):  # make buttons for each tile
        # set text to the tile number or a space if the tile is 0
        text = str(tiles.tiles[i]) if tiles.tiles[i] != 0 else ' '
        buttons.append(Button(gui, text=text, font=font, height=3,
                       width=5, padx=0, command=lambda i=i: clickButton(i)))  # make a button for each tile
        buttons[i].grid(row=i//4, column=i % 4, sticky='nesw')
        # set the background and foreground color
        buttons[i].config(bg='black', fg='black')
        gui.nametowidget(buttons[i].winfo_name()).grid(
            row=i//4, column=i % 4, sticky='nesw')
    shufflebutton = Button(gui, text='Shuffle', font=font, height=3,
                           width=5, padx=0, command=lambda: shuffle())  # make a button to shuffle the tiles
    shufflebutton.grid(row=4, column=0, columnspan=4,
                       sticky='nesw')  # place the button

    text = Label(
        gui, text='Click on a tile to move it. Click shuffle to shuffle the tiles.')
    text.grid(row=5, column=0, columnspan=4, sticky='nesw')  # place the text

    gui.mainloop()  # run the gui
