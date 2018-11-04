import tkinter
width = 640
height = 480
cx, cy, size = width / 2, height / 2, 60

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()
canvas.config(bg="gray")
canvas.create_text(cx, 20, text="Python Circle")

def circle():
    x, y = cx - size / 2, cy - size / 2
    canvas.create_oval(x - size / 2, y - size / 2, x + size / 2, y + size / 2)
    canvas.create_oval(x, y - size / 2, x + size, y + size / 2)
    canvas.create_oval(x + size / 2, y - size / 2,
                       x + 1.5 * size, y + size / 2)

    canvas.create_oval(x - size / 2, y, x + size / 2, y + size)
    canvas.create_oval(x, y, x + size, y + size, fill="yellow")
    canvas.create_oval(x + size / 2, y, x + 1.5 * size, y + size)

    canvas.create_oval(x - size / 2, y + size / 2,
                       x + size / 2, y + 1.5 * size)
    canvas.create_oval(x, y + size / 2, x + size, y + 1.5 * size)
    canvas.create_oval(x + size / 2, y + size / 2,
                       x + 1.5 * size, y + 1.5 * size)


def circle_f():
    size_f = size / 2
    x, y = cx - size_f, cy - size_f

    for i in range(0, 3):
        for j in range(0, 3):
            canvas.create_oval(x + i * size_f - size_f, y + j * size_f - size_f, x + i * size_f + size_f,
                               y + j * size_f + size_f)

    canvas.mainloop()


circle()
circle_f()
