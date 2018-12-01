##############################################################################
# The program do not nothing special, only shows paint a street homes via
# recursion with turtle
##############################################################################


import turtle
import time
import random
turtle.tracer(2, 1)
t = turtle.Turtle()


def home():
    t.pu()
    t.home()
    t.pd()


def wall(length, color_wall="red"):
    t.pencolor(color_wall)
    t.pensize(2)
    t.lt(90)
    t.pu()
    t.setx(x)
    t.sety(y)
    t.pd()

    def wall_r(n, length):
        if n == 0:
            return 0
        else:
            t.fd(length)
            t.rt(90)
            wall_r(n - 1, length)
    wall_r(4, length)
    home()


def top(length, color_top="brown"):
    t.pencolor(color_top)
    t.pensize(2)
    t.pu()
    t.setx(x)
    t.sety(y + length)
    t.pd()

    def top_r(n, length):
        if n == 0:
            pass
        else:
            t.fd(length)
            t.lt(120)
            top_r(n - 1, length)
    top_r(3, length)
    home()


def house(length, color_top, color_wall):
    wall(length, color_wall)
    top(length, color_top)


def street(n):
    global x
    # for i in range(10,80,2):
    #     length = i
    #     house(length,color_top,color_wall)
    #     x += length
    if n < 20:
        pass
    else:
        length = n
        house(length, color_top, color_wall)
        x += length
        street(n - 5)
        house(length, color_top, color_wall)
        x += length


x, y = -700, 50
length = 80
color_wall, color_top = "blue", "red"
# house(length, color_top, color_wall)
# top(length, color_top)
# street([10,20,50,20,80,100,55,68,30])
street(80)

time.sleep(3)
