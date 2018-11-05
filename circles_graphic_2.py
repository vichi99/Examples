import random
import tkinter
width = 640
height = 480
cx, cy, size = width / 2, height / 2, 10

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()
canvas.config(bg="gray")

def random_circles():
    for i in range(1000):
        x = random.randrange(width)
        y = random.randrange(height)

        if random.randint(0, 1):
            color_o = "red"
        else:
            color_o = "blue"
        if x > width / 2 and y > height / 2:
            color = "red"
        elif x > width / 2 and y <= height / 2:
            color = "green"
        elif x <= width / 2 and y > height / 2:
            color = "yellow"
        else:
            color = "purple"

        canvas.create_oval(x, y, x + size, y + size, outline=color_o, fill=color)
    canvas.mainloop()

def flag():
    for i in range(2000):
        x = random.randrange(width)
        y = random.randrange(height)

        if 0 <= y < height/2:
            color = "white"
        else:
            color = "red"

        canvas.create_oval(x, y, x + size, y + size, fill=color, outline = "")
    canvas.mainloop()
random_circles()
# flag()
