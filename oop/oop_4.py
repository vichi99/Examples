##############################################################################
# The program do not nothing special, only shows oop
##############################################################################


import tkinter
import random
class Square:
    canvas = None

    def __init__(self, x, y, size=40):
        self.size = size
        self.id = self.canvas.create_rectangle(x-size/2, y-size/2,
                                                x+size/2, y+size/2,
                                                fill="gray")
    def random_move(self):
        dx = random.randrange(-4, 5)
        dy = random.randrange(-4, 5)
        self.canvas.move(self.id, dx, dy)
def tik():
    for s in squares:
        s.random_move()
    Square.canvas.after(10, tik)
Square.canvas = tkinter.Canvas(width=640, height=480)
Square.canvas.pack()
squares = [Square(random.randrange(640), random.randrange(480)) for i in range(100)]
tik()
Square.canvas.mainloop()
