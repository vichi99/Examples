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


# counter char in the sentence
# counter = 0
# def count(char, sentence):
#     global counter
#     n = len(sentence)
#     if n == 0:
#         return
#     if sentence[n - 1] == char:
#         counter += 1
#     count(char, sentence[0:n - 1])

def count(char, sentence):
    if sentence == "":
        return 0
    if sentence[0] == char:
        return 1 + count(char, sentence[1:])
    else:
        return count(char, sentence[1:])


# def factorial(n):
#     global sum
#     if n <= 1:
#         return
#     sum *= n * (n - 1)
#     factorial(n - 2)

def factorial(n):
    if n < 2 :
        return 1
    else:
        return n * factorial(n-1)


# spiral(10)
# numbers(5)


# for i in range(10):
#     print("fib({}) => {}".format(i, fib(i)))


# for i in range(100):
#     print("fib({}) => {}".format(i, fib_better(i)))


# char = "m"
# sentence = "make made meal mm emma"
# print(count(char, sentence))

# for i in range(11):
#     sum=1
#     factorial(i)
#     print("factorial {} => {}".format(i,sum))

# for i in range(11):
#     print("factorial {} => {}".format(i,factorial(i)))
