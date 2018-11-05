import tkinter
import random

canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

number = random.randint(1, 6)
# number = int(input("Enter the number: "))
print("The number {} fell to a cube".format(number))

# size of cube
size = 200

# center of dice
x, y = canvas_width / 2, canvas_height / 2
unit = size / 5
radius = size * 0.03

# polygon
#    p2___p3
# p1/       \p4
#   |       |
#   |       |
# p8\_______/p5
#   p7    p6

p1 = x - size / 2,  y - size / 2 + radius
p2 = x - size / 2 + radius, y - size / 2
p3 = x + size / 2 - radius, y - size / 2
p4 = x + size / 2,  y - size / 2 + radius
p5 = x + size / 2,  y + size / 2 - radius
p6 = x + size / 2 - radius, y + size / 2
p7 = x - size / 2 + radius, y + size / 2
p8 = x - size / 2,  y + size / 2 - radius

canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                      outline="black", fill="gray", width=3)


#        a a a
#        1 2 3
#      +-------+
#   b1 | 1   2 |
#   b2 | 3 4 5 |
#   b3 | 6   7 |
#      +-------+

a1 = x - 1.5 * unit
a2 = x
a3 = x + 1.5 * unit

b1 = y - 1.5 * unit
b2 = y
b3 = y + 1.5 * unit

x1, y1 = a1, b1
x2, y2 = a3, b1
x3, y3 = a1, b2
x4, y4 = a2, b2
x5, y5 = a3, b2
x6, y6 = a1, b3
x7, y7 = a3, b3

if number == 1:
    dot = [(x4, y4)]
elif number == 2:
    dot = [(x2, y2), (x6, y6)]
elif number == 3:
    dot = [(x2, y2), (x4, y4), (x6, y6)]
elif number == 4:
    dot = [(x1, y1), (x2, y2), (x6, y6), (x7, y7)]
elif number == 5:
    dot = [(x1, y1), (x2, y2), (x4, y4), (x6, y6), (x7, y7)]
elif number == 6:
    dot = [(x1, y1), (x2, y2), (x3, y3), (x5, y5), (x6, y6), (x7, y7)]
for i in dot:
    x, y = i
    # print("x: " + str(x) + "  y: " + str(y))
    canvas.create_oval(x - unit / 2, y - unit / 2, x + unit / 2, y + unit / 2, fill="green")

canvas.mainloop()
