##############################################################################
# The program do not nothing special, only shows recursion with turtle
##############################################################################


import turtle
import time,random
turtle.tracer(20,0)
t = turtle.Turtle()
t.pencolor('maroon')
t.lt(90)

def tree(n):
    if n == 0:
        t.fd(30)
        t.bk(30)
    else:
        t.fd(30)
        t.lt(40)
        tree(n - 1)
        t.rt(80)
        tree(n - 1)
        t.lt(40)
        t.bk(30)


def tree_2(n, d):
    t.fd(d)
    if n > 0:
        t.lt(40)
        tree_2(n - 1, d * .7)
        t.rt(75)
        tree_2(n - 1, d * .6)
        t.lt(35)
    t.bk(d)

def tree_3(n, d):
    t.pensize(2 * n + 1)
    t.fd(d)
    if n == 0:
        t.dot(10, 'green')
    else:
        uhol1 = random.randint(20, 40)
        uhol2 = random.randint(20, 60)
        t.lt(uhol1)
        tree_3(n - 1, d * random.randint(40, 70) / 100)
        t.rt(uhol1 + uhol2)
        tree_3(n - 1, d * random.randint(40, 70) / 100)
        t.lt(uhol2)
    t.bk(d)


# tree(3)
# tree_2(5,80)
for i in range(30):
    x = random.randint(-300, 300)
    y = random.randint(-300, 100)
    t.pu()
    t.setpos(x,y)
    t.pd()
    tree_3(random.randint(3,7), random.randint(50,180))




time.sleep(2)
