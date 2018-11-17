##############################################################################
# The Hangman "Game"
##############################################################################
import tkinter
width, height = 640, 480

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()


def draw_gallows(x, y):
    gnd = (x - 60, y, x + 60, y)
    frame = (x, y, x, y - 250,
             x, y - 250, x + 140, y - 250,
             x + 140, y - 250, x + 140, y - 200)
    canvas.create_line(gnd, width=10)
    canvas.create_line(frame, width=5)


def draw_hangman(x, y, r):
    head = (x + 140 - r, y - 200, x + 140 + r, y - 200 + 2 * r)
    canvas.create_oval(head, width=3)


draw_gallows(width / 2, height / 2 + 150)
draw_hangman(width / 2, height / 2 + 150, 20)

canvas.mainloop()
