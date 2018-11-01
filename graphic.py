import tkinter
width = 640
height = 480
cx, cy, size = width/2, height/2, 60
x, y = cx-size, cy-size

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()
canvas.config(bg="gray")
canvas.create_text(cx, 20, text="Python Circle")

#canvas.create_rectangle(x, y, x+size, y+size)
canvas.create_oval(x-size/2, y-size/2, x+size/2, y+size/2)
canvas.create_oval(x, y-size/2, x+size, y+size/2)
canvas.create_oval(x+size/2, y-size/2, x+1.5*size, y+size/2)

canvas.create_oval(x-size/2, y, x+size/2, y+size)
canvas.create_oval(x+size/2, y, x+1.5*size, y+size)

canvas.create_oval(x-size/2, y+size/2, x+size/2, y+1.5*size)
canvas.create_oval(x, y+size/2, x+size, y+1.5*size)
canvas.create_oval(x+size/2, y+size/2, x+1.5*size, y+1.5*size)

size=size
for i in range(0,3):
    for j in range(0,3):
        canvas.create_oval(x+i*size-size, y+j*size-size, x+i*size+size,
        y+j*size+size)

#canvas.create_oval(x, y, x+120, y+120,fill="yellow")


canvas.mainloop()
