from tkinter import *

gui = Tk()            # make a window class

topframe = Frame(gui)  # make a frame
topframe.pack()       # add the frame to the window

# make buttons and add them to the frame
# when you make a button you can specify its height, width, background and foreground colors
yellowb = Button(topframe, width=25, height=5, text="Yellow", bg="yellow")
yellowb.pack(side=RIGHT)

greenb = Button(topframe, width=25, height=5, text="Green", bg="green")
greenb.pack(side=LEFT)

blueb = Button(topframe, width=25, height=5, text="Blue", bg="blue", fg="red",)
blueb.pack(side=LEFT)

# make another frame and buttons and add them to the frame
bottomframe = Frame(gui)
bottomframe.pack(side=BOTTOM)


pinkb = Button(bottomframe, width=25, height=5, text="Pink", bg="pink")
pinkb.pack(side=LEFT)

redb = Button(bottomframe, width=25, height=5, text="Red", bg="red")
redb.pack(side=LEFT)

blackb = Button(bottomframe, width=25, height=5,
                text="Black", bg="black", fg="white",)
blackb.pack(side=RIGHT)

gui.mainloop()    # update the window
