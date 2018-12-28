##############################################################################
# The program do not nothing special, only shows events with bind
##############################################################################
import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def B1_press(event):
    print("Press button 1 on x={}, y={}".format(event.x, event.y))


def B1_release(event):
    print("Release button 1 on x={}, y={}".format(event.x, event.y))


def B1_drag(event):
    print("Drag button 1 on x={}, y={}".format(event.x, event.y))


def mouse_motion(event):
    print("mouse motion on on x={}, y={}".format(event.x, event.y))


def create_rect(event):
    global rect_id
    rect_id = canvas.create_rectangle(event.x, event.y, event.x, event.y)


def keybord(event):
    print(repr(event))


# canvas.bind('<ButtonPress-1>', B1_press)
# canvas.bind('<ButtonRelease-1>', B1_release)
# canvas.bind('<B1-Motion>', B1_drag)
# canvas.bind('<Motion>', mouse_motion)
# canvas.bind('<ButtonPress-1>', create_rect)
# canvas.bind_all('<Key>',keybord)

##################################################
# Create rectangle via drag mouse
##################################################

def create_oval(event):
    canvas.create_oval(event.x - 20, event.y - 20,
                       event.x + 20, event.y + 20)


def mouse_drag(event):
    x1, y1, x2, y2 = canvas.coords(rect_id)
    canvas.coords(rect_id, x1, y1, event.x, event.y)

# rect_id = None
# canvas.bind('<ButtonPress-1>', create_oval)
# canvas.bind('<B1-Motion>', mouse_drag)


##################################################
# painting via darts
##################################################

def paint():
    global coordinates
    coordinates += [x, y]
    canvas.coords(line_id, coordinates)


def left(event):
    global x
    x -= 10
    paint()


def right(event):
    global x
    x += 10
    paint()


def up(event):
    global y
    y -= 10
    paint()


def down(event):
    global y
    y += 10
    paint()


x, y = 100, 100
coordinates = [x, y]
line_id = canvas.create_line(0, 0, 0, 0)
# canvas.bind_all('<Left>', left)
# canvas.bind_all('<Right>', right)
# canvas.bind_all('<Up>', up)
# canvas.bind_all('<Down>', down)


canvas.mainloop()
