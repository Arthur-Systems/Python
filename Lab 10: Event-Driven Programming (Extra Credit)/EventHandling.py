from tkinter import *


def change_text(event):     # this is an event handler
    global message
    if message.get() == 'You clicked me!':
        message.set('Click me again!')
    else:
        message.set('You clicked me!')


# main program
gui = Tk()                # make a GUI window
message = StringVar()     # make a variable string
message.set('Click me')
button = Button(textvariable=message, width=25,
                height=5, bg='bisque', fg='black')
# bind the event clicking the button to the event handler change_text
button.bind('<Button-1>', change_text)
button.pack()
# update the program state (check for new events and run event handlers)
mainloop()
