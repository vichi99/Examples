##############################################################################
# The program do not nothing special, only shows events with bind
##############################################################################
import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

def B1_press(event):
    text = "(" + str(event.x) + "," + str(event.y) + ")"
    canvas.create_text(event.x, event.y,text=text, font='Helvetica 12')

# canvas.bind('<ButtonPress-1>',B1_press)


def rect(x=100,y=100):
    global dirc
    coordinates = x, y
    size = 50
    for i in range(1,9):
        canvas.create_rectangle(x,y,x + size,y + size)
        coordinates = [x,y]
        dirc = { i : coordinates}
        print("{} dir {}".format(i, dirc[i][0]))
        x = x+size
dirc = {}
rect()
canvas.mainloop()
