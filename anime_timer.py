##############################################################################
# The program do not nothing special, only show timer
##############################################################################
import tkinter
from datetime import datetime

#init
##########################################
width,height = 400,200
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

timer = canvas.create_text(width/2, height/2, text="", font='Helvetica 20')
size = 10
def clock():
    global size
    size = size + 2
    font = 'Helvetica {}'.format(size)
    time = datetime.utcnow().strftime('%H:%M:%S.%f')[:-5]
    canvas.itemconfig(timer, text= time,font= font)
    if size == 40:
        size = 10
    canvas.after(100, clock)

clock()

canvas.mainloop()
