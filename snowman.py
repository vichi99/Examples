import tkinter
name = "Snowman"
width = 640
height = 480

r = 90
width_button = r / 10
width_eyes = width_button / 2
width_mouth = width_button / 2.5
x, y = width / 2 - r, height - 2 * r

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()
canvas.config(bg="light blue")
canvas.create_text(width / 2, 30, text=name,
                   font="Monaco 25", fill="black")
canvas.create_rectangle(width / 2, height / 2,
                        (width / 2), (height / 2), width=10)


def ball(x, y, r):
    coordinates = (x, y, x + 2 * r, y + 2 * r)
    canvas.create_oval(coordinates, width=2, outline='', fill="white")


def button(x, y, r):
    x = x + r
    for i in [r / 2, r, r * 1.5]:
        canvas.create_oval(x, y + i, x, y + i, width=width_button)


def face(x, y, r):
    x1 = x + r / 2
    y1 = y + r / 2
    x2 = x1 + r
    for x, y in [[x1, y1], [x2, y1], [x + r, y + r]]:
        canvas.create_oval(x, y, x, y, width=width_mouth)
    y2 = y + r / 2
    canvas.create_line(x1, y2, x2, y2, width=width_mouth)


def snowman(x, y, r):
    ball(x, y, r)
    button(x, y, r)
    x = x + r / 2 * 2 / 3
    y = y - r * 2 / 3 * 2
    r = r * 2 / 3
    ball(x, y, r)
    button(x, y, r)
    x = x + r / 2 * 2 / 2
    y = y - r * 1 / 2 * 2
    r = r * 1 / 2
    ball(x, y, r)
    face(x, y, r)


# ball(x,y+height/4,r)
snowman(x, y, r)


canvas.mainloop()
