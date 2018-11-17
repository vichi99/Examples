##############################################################################
# The program shows many circles
##############################################################################

import tkinter
import random

width = 640
height = 480

canvas = tkinter.Canvas(width=width, height=height, bg="gray")
canvas.pack()


def paint_circle(x, y, size, color):
    coordinates = x - size / 2, y - size / 2, x + size / 2, y + size / 2
    canvas.create_oval(coordinates, fill=color)


def size_def(x, y):
    return ((x - width / 2)**2 + (y - height / 2)**2)**.5


def color_def(size):
    x = 255 - int((size / 400) * 255)
    return '#{:02x}{:02x}{:02x}'.format(x, x, x)


for x in range(2000):
    x = random.randrange(width)
    y = random.randrange(height)
    size = size_def(x, y)
    color = color_def(size)
    paint_circle(x, y, size / 4, color)

canvas.mainloop()
