import tkinter
name = "Snowman"
width = 640
height = 480
r = 100
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


def snowman(x, y, r):
    ball(x, y, r)
    x = x + r / 2 * 2 / 3
    y = y - r * 2 / 3 * 2
    r = r * 2 / 3
    ball(x, y, r)
    x = x + r / 2 * 2 / 2
    y = y - r * 1 / 2 * 2
    r = r * 1 / 2
    ball(x, y, r)


# ball(x,y+height/4,r)
snowman(x, y, r)


canvas.mainloop()
