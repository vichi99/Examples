##############################################################################
# The program do not nothing special, only shows oop
##############################################################################
import tkinter
import random

class CanvasBox:

    def __init__(self, width = 640, height = 480):
        self.canvas = tkinter.Canvas(width=width, height=height)
        self.canvas.pack()

    def MainLoop(self):
        self.canvas.mainloop()

class Square:
    def __init__(self, canvas, x = 40, y = 40 , size=40):
        self.cor_x = x
        self.cor_y = y
        self.size = size
        self.canvas = canvas


    def paint(self):
        size = self.size
        x = self.cor_x
        y = self.cor_y
        self.id = self.canvas.create_rectangle(x-size/2, y-size/2,x+size/2, y+size/2,fill="gray")
