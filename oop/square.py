##############################################################################
# The program do not nothing special, only shows oop
##############################################################################
import random
from lib import * #CanvasBox,Square
width,height,size = 100, 100, 40

def test():
    box = Square(dashboard.canvas)
    box.cor_x = random.randrange(size , width - size)
    box.cor_y = random.randrange(size , height - size)
    box.size = size
    box.paint()

dashboard = CanvasBox(width = width , height = height)
dashboard_2 = CanvasBox(width = width , height = height)

#boxes = [test() for i in range(100)]

rectangle_1 = Square(dashboard.canvas)
rectangle_1.canvas
rectangle_1.cor_x = 0
rectangle_1.cor_y = 0
rectangle_1.size = 100
rectangle_1.paint("red")


Legatee = Square(dashboard_2.canvas)
Legatee.canvas
Legatee.cor_x = 0
Legatee.cor_y = 0
Legatee.size = 100
Legatee.paint("blue")

dashboard.MainLoop()
dashboard_2.MainLoop()
