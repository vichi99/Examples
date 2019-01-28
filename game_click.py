##############################################################################
# The game: click on circle in interval
##############################################################################
import tkinter,random


#init
##########################################
width,height = 640,480
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

#def
##########################################

def circle_make():
    global x,y,state
    x = random.randint(20,width - (d +10))
    y = random.randint(20,height - (d +10))
    coord= x,y,x+d,y+d
    canvas.coords(circle,coord)
    state = "on"
    canvas.after(1000,circle_make)


def mouse_click(event):
    global score_count
    global state
    x1 = x + (d/2)
    y1 = y + (d/2)
    x2 = event.x
    y2 = event.y
    # print("x1: {}, y1: {}\nx2: {}, y2= {}".format(x1,y1,x2,y2))
    distance = abs(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
    if distance <= d/2: #if click is inside the circle
        if state == "on":
            score_count += 1
            state = "off"
    else:
        score_count -= 1
    score_refresh()

def score_refresh():
    score_text = "Score: {}".format(score_count)
    canvas.itemconfig(score_canvas,text = score_text)

#making
##########################################
d=80
x,y=0,0
score_count = 0
score_text = "Score: {}".format(score_count)
state = "on" # condition for doubleclick if click is in the circle
circle = canvas.create_oval(x,y,d,d,fill= "green")
score_canvas = canvas.create_text(70, 20, text=score_text, font='Helvetica 22')

circle_make()

canvas.bind('<ButtonPress-1>', mouse_click)

canvas.mainloop()
