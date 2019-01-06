##############################################################################
# The program do not nothing special, only shows function after via animation
##############################################################################
import tkinter, random, math
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

# tik tok
##########################################
def tik():
    print("tik")
    canvas.after(500, tok)
def tok():
    print("tok")
    canvas.after(500, tik)
# tik()
##########################################



# oval moving left - right
##########################################
def oval():
    global direction
    x1,y1,_,_ = canvas.coords(oval_id_1)
    if x1 <= 0:
        direction = 1
    elif x1+40 >= 640:
        direction = -1
    canvas.move(oval_id_1, direction*5,0)
    canvas.after(10, oval)

def oval_color():
    color = "#{:06x}".format(random.randrange(256**3))
    canvas.itemconfig(oval_id_1, fill=color)
    canvas.after(500, oval_color)

direction = 1
oval_id_1 = ()
oval_id_1 = canvas.create_oval(100,100, 140, 140)
oval()
oval_color()
##########################################

# oval moving around mouse
##########################################
def tikk():
    global angle
    angle = (angle+5) % 360
    x = cx + math.cos(math.radians(angle))*40
    y = cy + math.sin(math.radians(angle))*40
    canvas.coords(oval_id_2, x-20, y-20, x+20, y+20)
    canvas.after(10, tikk)
def tokk():
    color = "#{:06x}".format(random.randrange(256**3))
    canvas.itemconfig(oval_id_2, fill=color)
    canvas.after(500, tokk)
def mouse_move(event):
    global cx,cy
    cx = event.x
    cy = event.y
canvas.bind("<Motion>", mouse_move)
cx = 320
cy = 240
angle = 0
oval_id_2 = ()
oval_id_2 = canvas.create_oval(cx-20, cy-20, cx+20, cy+20)
tikk()
tokk()




##########################################
canvas.mainloop()
