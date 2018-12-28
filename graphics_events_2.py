##############################################################################
# The program do not nothing special, only shows events with bind
##############################################################################
import tkinter
import random

width,height = 640,480
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()


# create text
#################################
def B1_press(event):
    text = "(" + str(event.x) + "," + str(event.y) + ")"
    canvas.create_text(event.x, event.y, text=text, font='Helvetica 12')

# canvas.bind('<ButtonPress-1>',B1_press)
#################################



# create box with filling on click
#################################
def rect(x,y,size,count):
    coordinates = x, y
    for i in range(0,count):
        canvas.create_rectangle(x, y, x + size, y + size)
        x = x + size


def click(event):
    order_x = ((event.x - x) // size)+1
    order_y = ((event.y - y) // size)+1
    if 0 < order_x <= count and order_y == 1:
        # print("x = {} ==> x={} y={} ".format(event.x, order_x,order_y))
        x0 = x + ((order_x - 1 )*size)
        y0 = y + ((order_y - 1 )*size)
        canvas.create_rectangle(x0, y0, x0 + size, y0 + size, fill = "red")

x,y,size,count = 100,100,50,10
# rect(x,y,size,count)
# canvas.bind('<ButtonPress-1>', click)
#################################

# create and drag square_id
#################################
def press_move(event):
    global coordinates
    coordinates = (event.x,event.y)

# def B1_drag(event):
#     global coordinates
#     if (coordinates[0]-25) < event.x < (coordinates[0]+25) and (coordinates[1]-25) < event.y < (coordinates[1]+25):
#         canvas.move(square_id, event.x - coordinates[0], event.y - coordinates[1])
#         coordinates = (abs(event.x), abs(event.y))

x_square, y_square = width/2, height/2
coordinates = [x_square , y_square]
# square_id = canvas.create_rectangle(x_square - 25, y_square - 25,x_square + 25,
                                # y_square + 25)

## canvas.bind('<ButtonPress-1>', press_move)
# canvas.bind('<B1-Motion>', B1_drag)
#################################


# random keyboard
#################################
def key(event):
    random_x = random.randint(20, height - 20)
    random_y = random.randint(20, height - 20)
    canvas.create_text(random_x, random_y, text=event.char, font='Helvetica 12')

# canvas.bind_all('<Key>', key)

#################################

canvas.mainloop()
