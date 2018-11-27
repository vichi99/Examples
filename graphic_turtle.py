##############################################################################
# The program shows couple function with turtle
##############################################################################
import turtle
import time
import random

width, height = 500, 500

# DEF SHAPE


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.rt(90)


def circle(t, radius):
    # for i in range(180):
    #     t.fd(length)
    #     t.rt(2)
    t.circle(radius)


def move(t):
    t.pu()
    t.setpos(random.randint(-width / 2, width / 2),
             random.randint(-height / 2, height / 2))
    t.seth(random.randrange(360))
    t.pd()


def set_turtle(t):
    turtle.delay(0)
    t.speed(10)
    t.pensize(2)
    t.pencolor("red")
    t.fillcolor("blue")
    t.ht()


def set_delay_speed(t, delay, speed):
    turtle.delay(delay)
    t.speed(speed)


def set_zero(t):
    t.pu()
    t.setpos(0, 0)
    t.pd()
    t.clear()

# DEF FUNCTION


def func_circle(t):
    set_zero(t)
    set_turtle(t)
    set_delay_speed(t, 1, 5)  # delay, speed
    for i in range(10):
        t.begin_fill()
        move(t)
        square(t, 30)
        circle(t, 15)

        if random.randrange(2):
            t.end_fill()


def spiral_1(t):
    set_zero(t)
    set_turtle(t)
    set_delay_speed(t, 1, 0)  # delay, speed
    for angle in range(30, 180):
        print(angle)
        for i in range(2, 200, 3):
            t.fd(i)
            t.rt(angle)
        set_zero(t)


def spiral_2(t):
    set_zero(t)
    set_turtle(t)
    # set_delay_speed(0,0) #delay, speed
    turtle.tracer(5, 0)  # every second, delay
    for i in range(1, 5):
        i /= 10
        t.setpos(0, 0)
        # print(t.xcor())
        # print(t.ycor())
        for angle in range(5000):
            t.fd(6)
            t.rt(angle + i)
            if -1 < t.xcor() < 1 and -1 < t.ycor() < 1:
                time.sleep(2)
                break
        t.clear()


def spiral_3(t):
    set_zero(t)
    # set_delay_speed(0,0) #delay, speed
    turtle.tracer(10, 0)  # every second, delay
    for i in range(1, 10):
        i /= 100
        t.pu()
        t.setpos(0, 0)
        t.pd()
        for angle in range(10000):
            t.fd(6)
            t.rt(angle + i)
        time.sleep(2)
        t.clear()


def test(t):
    set_zero(t)
    turtle.tracer(0)
    turtles = [turtle.Turtle() for x in range(100)]
    for i in turtles:
        move(i)
        square(i, 40)
        turtle.update()


def paralel_turtle(t):
    set_zero(t)
    turtle.tracer(0)
    turtles = []
    for i in range(60):
        turtles.append(turtle.Turtle())
        turtles[-1].seth(i * 6)

    for i in range(180):
        for t in turtles:
            t.fd(5)
            t.rt(2)
        turtle.update()


def following_turtles(t):
    set_zero(t)
    n = 10
    turtles = []
    turtle.tracer(0)
    for i in range(n):
        t = turtle.Turtle()
        t.pensize(3)
        t.pencolor("#{:06x}".format(random.randrange(256 ** 3)))
        # t.seth(random.randrange(5,10))
        move(t)
        turtles.append(t)
    while True:
        for i in range(n):
            j = (i + 1) % n
            angle = turtles[i].towards(turtles[j])
            dist = turtles[i].distance(turtles[j])
            turtles[i].seth(angle)
            turtles[i].fd(dist / 200)
        turtle.update()


t = turtle.Turtle()
turtle.bgcolor("yellow")


def run_all():
    function = [func_circle(t), spiral_1(t), spiral_2(t), spiral_3(t),
                test(t), paralel_turtle(t), following_turtles(t)]
    for i in function:
        i
        time.sleep(2)
# func_circle(t)
spiral_1(t)
# spiral_2(t)
# spiral_3(t)
# test(t)
# paralel_turtle(t)
# following_turtles(t)


time.sleep(3)

# metóda	       variant	                význam
# forward(d)	   fd	                    choď dopredu
# back(d)   	   backward, bk	            cúvaj
# right(u)	       rt	                    otoč sa vpravo
# left(u)   	   lt	                    otoč sa vľavo
# penup()   	   pu, up	                zdvihni pero
# pendown() 	   pd, down	                spusti pero
# setpos(x, y)     setposition, goto	    choď na pozíciu
# pos()	position	                        zisti pozíciu korytnačky
# xcor()		                            zisti x-ovú súradnicu
# ycor()		                            zisti y-ovú súradnicu
# heading()		                            zisti uhol korytnačky
# setheading(u)    seth	                    nastav uhol korytnačky
# pensize(h)       width               	    nastav hrúbku pera
# pencolor(f)		                        nastav farbu pera
# pencolor()		                        zisti farbu pera
# fillcolor(f)                      		nastav farbu výplne
# fillcolor()                       		zisti farbu výplne
# color(f1, f2)                     		nastav farbu pera aj výplne
# color()                           		zisti farbu pera aj výplne
# reset()                           		zmaž kresbu a inicializuj korytnačku
# clear()                           		zmaž kresbu
# begin_fill()                         		začiatok budúceho vyfarbenia
# end_fill()                        		koniec vyfarbenia
#.shape()
