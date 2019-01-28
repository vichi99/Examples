##############################################################################
# The program do not nothing special, only shows oop
##############################################################################
import tkinter

class CanvasBox:
    canvas = None

    def __init__(self, width = 640, height = 480):

        self.canvas = tkinter.Canvas(width=width, height=height)
        self.canvas.pack()
        #self.canvas.mainloop()
