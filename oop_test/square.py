##############################################################################
# The program do not nothing special, only shows oop
##############################################################################
#import tkinter
from CanvasBox import CanvasBox

class Square():
    canvas = None
    def __init__(self, x = 40, y = 40 , size=40, width = 640, height = 480):
        self.cor_x = x
        self.cor_y = y
        self.size = size
        self.width = width
        self.height = height


    def paint(self):
        self.canvas = CanvasBox(self.width,self.height).canvas
        size = self.size
        x = self.cor_x
        y = self.cor_y
        self.id = self.canvas.create_rectangle(x-size/2, y-size/2,x+size/2, y+size/2,fill="gray")

    def loop(self):
        self.canvas.mainloop()

box = Square()
#box.cor_x = 200
box.paint()

box.loop()
