import turtle,time,random
turtle.tracer(10,0)
t = turtle.Turtle()

def home():
    t.pu()
    t.home()
    t.pd()

def wall(length,color_wall="red",x=0,y=0):
    n=4
    t.pencolor(color_wall)
    t.pensize(2)
    t.lt(90)
    t.pu()
    t.setx(x)
    t.sety(y)
    t.pd()
    def wall_r(n,length,color_wall):
        if n == 0:
            return 0
        else:
            t.fd(length)
            t.rt(90)
            wall_r(n -1,length,color_wall)
    wall_r(n, length,color_wall)
    home()

def top(length, color_top="brown",x=0, y=0):
    n=3
    t.pencolor(color_top)
    t.pensize(2)
    t.pu()
    t.setx(x)
    t.sety(y+length)
    t.pd()
    def top_r(n, length, color_top):
        if n == 0:
            return 0
        else:
            t.fd(length)
            t.lt(120)
            top_r(n-1,length,color_top)
    top_r(n, length, color_top)
    home()



def house(length,color_top,color_wall):
    # wall(length,color_wall,x,y)
    top(length,color_top,x,y)

x,y= -100,50
# length=80
color_wall,color_top="blue","red"
for i in range(5):
    # x,y=random.randrange(10,300),random.randrange(200,500)
    x += 50
    length=random.randrange(30,50)
    house(length,color_top,color_wall)


time.sleep(4)
