import turtle
# turtle.delay(10)
# t=turtle.Turtle()
# t.speed(0)

# def spiral(d):
#     if d > 100:
#         t.pencolor("red")
#     else:
#         t.fd(d)
#         t.lt(60)
#         spiral(d+3)
#         t.fd(d)
#         t.rt(60)

def numbers(n):
    if n < 1 :
        pass
    else:
        print(n, end=", ")
        numbers(n-1)
        print(n,end=", ")
numbers(15)

# spiral(10)
