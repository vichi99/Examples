##############################################################################
# The program shows interesting circles,box, cube and flag
##############################################################################

import tkinter
import random

width = 640
height = 480

size = 60  # "d" size of circles

size_cu = 120  # size of cubes

size_flag = 5  # size of circles in flag

size_mic = 100  # size of symbol microsoft
size_mic_c = 3  # size of circles in symbol

# import tkinter
# main = tkinter.Tk()
# canvas = tkinter.Canvas(main)
# canvas.pack()
# main.mainloop()

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()
canvas.config(bg="gray")
canvas.create_text(width / 2, 30, text="Python",
                   font="Monaco 25", fill="black")


def circle():
    cx, cy = width / 4, height / 4
    x, y = cx - size / 2, cy - size / 2
    canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2)
    canvas.create_oval(x, y - size / 2, x + size, y + size / 2)
    canvas.create_oval(x + size / 2, y - size / 2,
                       x + 1.5 * size, y + size / 2)

    canvas.create_oval(x - size / 2, y, x + size / 2, y + size)
    canvas.create_oval(x, y, x + size, y + size,
                       fill="yellow", outline="red", width=5)
    canvas.create_oval(x + size / 2, y, x + 1.5 * size, y + size)

    canvas.create_oval(x - size / 2, y + size / 2,
                       x + size / 2, y + 1.5 * size)
    canvas.create_oval(x, y + size / 2, x + size, y + 1.5 * size)
    canvas.create_oval(x + size / 2, y + size / 2,
                       x + 1.5 * size, y + 1.5 * size)


def circle_f():
    cx, cy = width / 4 * 3, height / 4
    size_f = size / 2
    x, y = cx - size_f, cy - size_f

    for i in range(0, 3):
        for j in range(0, 3):
            canvas.create_oval(x + i * size_f - size_f, y + j * size_f - size_f,
                               x + i * size_f + size_f,
                               y + j * size_f + size_f, width=4)


def cube():
    number = random.randint(1, 6)
    print("The number {} fell to a cube".format(number))

    # center of dice
    x, y = width / 4, height / 4 * 3
    unit = size_cu / 5
    radius = size_cu * 0.03

    # polygon
    #    p2___p3
    # p1/       \p4
    #   |       |
    #   |       |
    # p8\_______/p5
    #   p7    p6

    p1 = x - size_cu / 2,  y - size_cu / 2 + radius
    p2 = x - size_cu / 2 + radius, y - size_cu / 2
    p3 = x + size_cu / 2 - radius, y - size_cu / 2
    p4 = x + size_cu / 2,  y - size_cu / 2 + radius
    p5 = x + size_cu / 2,  y + size_cu / 2 - radius
    p6 = x + size_cu / 2 - radius, y + size_cu / 2
    p7 = x - size_cu / 2 + radius, y + size_cu / 2
    p8 = x - size_cu / 2,  y + size_cu / 2 - radius

    canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                          outline="black", fill="gray", width=3)

    #        a a a
    #        1 2 3
    #      +-------+
    #   b1 | 1   2 |
    #   b2 | 3 4 5 |
    #   b3 | 6   7 |
    #      +-------+

    a1 = x - 1.5 * unit
    a2 = x
    a3 = x + 1.5 * unit

    b1 = y - 1.5 * unit
    b2 = y
    b3 = y + 1.5 * unit

    x1, y1 = a1, b1
    x2, y2 = a3, b1
    x3, y3 = a1, b2
    x4, y4 = a2, b2
    x5, y5 = a3, b2
    x6, y6 = a1, b3
    x7, y7 = a3, b3

    if number == 1:
        dot = [(x4, y4)]
    elif number == 2:
        dot = [(x2, y2), (x6, y6)]
    elif number == 3:
        dot = [(x2, y2), (x4, y4), (x6, y6)]
    elif number == 4:
        dot = [(x1, y1), (x2, y2), (x6, y6), (x7, y7)]
    elif number == 5:
        dot = [(x1, y1), (x2, y2), (x4, y4), (x6, y6), (x7, y7)]
    elif number == 6:
        dot = [(x1, y1), (x2, y2), (x3, y3), (x5, y5), (x6, y6), (x7, y7)]
    for i in dot:
        x, y = i
        # print("x: " + str(x) + "  y: " + str(y))
        canvas.create_oval(x - unit / 2, y - unit / 2, x +
                           unit / 2, y + unit / 2, fill="red",
                           outline="blue", width=3)


def flag():
    for i in range(5000):
        x = random.randrange(width / 2, width)
        y = random.randrange(height / 2, height)

        # y = ax + b
        c1 = ((height * x) / width) - y
        c2 = (((-height * (x - width / 2) / width) + height - y))
        if c1 <= 0 and c2 >= 0:
            color = "blue"
        elif 0 <= y < height / 4 * 3:
            color = "white"
        else:
            color = "red"

        canvas.create_oval(x, y, x + size_flag, y +
                           size_flag, fill=color, outline="")


def microsoft():
    for i in range(1000):
        cx, cy = width / 2, height / 4
        x = random.randrange(cx - size_mic / 2, cx + size_mic / 2)
        y = random.randrange(cy - size_mic / 2, cy + size_mic / 2)

        # if random.randint(0, 1):
        #     color_o = "red"
        # else:
        #     color_o = "blue"
        if x <= cx and y <= cy:
            color = "red"
        elif x >= cx and y <= cy:
            color = "green"
        elif x <= cx and y >= cy:
            color = "blue"
        else:
            color = "yellow"

        canvas.create_oval(x, y, x + size_mic_c, y + size_mic_c,
                           outline="", fill=color)


circle()
circle_f()
cube()
flag()
microsoft()

canvas.mainloop()
