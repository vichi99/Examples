##############################################################################
# The program do not nothing special, only shows recursion
##############################################################################


import turtle
turtle.delay(10)
t = turtle.Turtle()
t.speed(0)


def spiral(d):
    if d > 100:
        t.pencolor("red")
    else:
        t.fd(d)
        t.lt(60)
        spiral(d + 3)
        t.fd(d)
        t.rt(60)


def numbers(n):
    if n < 1:
        pass
    else:
        print(n, end=", ")
        numbers(n - 1)
        print(n, end=", ")

# Fibonacci retracement


def fib(n):  # this is a bad example or we can use decorator
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


cache = {}


def fib_better(n):  # this is a better example, we write value to dict
    if n in cache:
        return cache[n]
    if n < 2:
        return 1
    else:
        x = fib_better(n - 1) + fib_better(n - 2)
        cache[n] = x
        return x


def chars(char,sentence):
    counter = 0
    n = len(sentence)
    def count(char,sentence,n):
        global counter
        if n == -1:
            return
        if sentence[n-1] == char:
            counter += 1
        count(char, sentence[n-1],n-1)
    count(char,sentence)
    print(counter)


char = "m"
sentence = "mama"
chars(char,sentence)



# spiral(10)
# numbers(5)


# for i in range(10):
#     print("fib({}) => {}".format(i, fib(i)))


# for i in range(100):
#     print("fib({}) => {}".format(i, fib_better(i)))
