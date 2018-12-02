##############################################################################
# The program do not nothing special, only shows events with bind
##############################################################################
import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def event_example(event):
    print(repr(event))


canvas.bind('<ButtonPress-1>', event_example)
# canvas.bind("ButtonPress1",event_example)
canvas.mainloop()
