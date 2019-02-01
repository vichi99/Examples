import turtle,time
import random
class Rect(turtle.Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.speed(0)
        self.pu()
        self.setpos(x, y)
        self.pd()
    def rectangle(self, size):
        for i in range(4):
            self.fd(size)
            self.rt(90)

class Wave(Rect):
    def fd(self, size):
        while size >= 5:
            self.lt(60)
            super().fd(5)
            self.rt(120)
            super().fd(5)
            self.lt(60)
            size -= 5
        super().fd(size)

class Crook(Rect):
    def fd(self, size):
        super().fd(size)
        self.rt(180 - random.randint(-3, 3))
        super().fd(size)
        self.rt(180 - random.randint(-3, 3))
        super().fd(size)

# t1 = Rect(-130, 0)
# t2 = Wave(0, 0)
# t3 = Crook(130, 0)
# t1.rectaWngle(100)
# t2.rectangle(100)
# t3.rectangle(100)

turtle.tracer(0)
curves = []
for x in range(-350, 350 , 50):
    for y in range(-350, 350 , 50):
        c = Crook(x,y)
        c.ht()
        curves.append(c)

for c in curves:
    c.rectangle(50)
    turtle.update()

turtle.mainloop()
