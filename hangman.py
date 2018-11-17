##############################################################################
# The Hangman "Game"
##############################################################################
import tkinter
width, height = 640, 480

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()


def draw_gallows(x, y):
    gnd = (x - 75, y, x + 75, y)
    frame = (x, y, x, y - 150, x, y - 150, x + 100, y - 150)
    canvas.create_line(gnd, width=10)
    canvas.create_line(frame, width=5)


draw_gallows(width / 2, height / 2 + 100)


canvas.mainloop()
