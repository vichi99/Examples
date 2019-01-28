##############################################################################
# The program do not nothing special, only shows oop
##############################################################################
import random
from lib import * #CanvasBox,Square
width,height,size = 500, 500, 40

def test():
    box = Square(dashboard.canvas)
    box.cor_x = random.randrange(size , width - size)
    box.cor_y = random.randrange(size , height - size)
    box.size = size
    box.paint()

dashboard = CanvasBox(width = width , height = height)


boxes = [test() for i in range(100)]


dashboard.MainLoop()
