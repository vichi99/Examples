##############################################################################
# The program do not nothing special, only show moving square
##############################################################################
import tkinter,random

#init
##########################################
width,height = 400,400
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

#make square
##########################################
def square_move():
    if status == "on":
        global direction
        x1,y1,x2,y2 = canvas.coords(square)
        if y1 <= 0:
            direction = 1
        elif y1+ (size) >= height:
            direction = -1
        canvas.move(square, 0,direction*5)
    canvas.after(10, square_move)

def square_color():
    if status == "on":
        color = "#{:06x}".format(random.randrange(256**3))
        canvas.itemconfig(square,fill = color)
    canvas.after(500,square_color)


direction= 1
size=30
x1,y1= width/2-(size/2),height/2-(size/2)
x2,y2 = width/2+(size/2),height/2+(size/2)

square = canvas.create_rectangle(x1,y1,x2,y2,width=0,fill= "black")


#action on click
##########################################
status = "off"
def B1_press(event):
    global status
    if status == "off":
        status = "on"
    else:
        status = "off"

#action
##########################################
square_color()
square_move()
canvas.bind('<ButtonPress-1>', B1_press)











canvas.mainloop()
