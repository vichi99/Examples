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


    def paint(self, color = "gray"):
        size = self.size
        x = self.cor_x
        y = self.cor_y
        self.id = self.canvas.create_rectangle(x,y,x+size,y+size,fill=color)

class Legatee(Square):
    pass

class Hi:
    def __init__(self,word):
        print(word + " :Hi super")

class Bu(Hi):
    def __init__(self,word):
        super().__init__(word)
        print(word)
