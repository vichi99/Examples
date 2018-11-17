##############################################################################
# The Hangman "Game"
##############################################################################
import tkinter
width, height = 640, 480

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()


def draw_gallows(x, y):
    gnd = (x - 60, y, x + 60, y)
    frame = (x, y, x, y - 250,
             x, y - 250, x + 140, y - 250,
             x + 140, y - 250, x + 140, y - 200)
    canvas.create_line(gnd, width=10)
    canvas.create_line(frame, width=5)


def draw_hangman(x, y, r):
    width = 3
    head = (x + 140 - r, y - 200, x + 140 + r, y - 200 + 2 * r)
    torso = (x + 140, y - 200 + 2 * r, x + 140, y - 200 + 2 * r + 80)
    larm = (x + 140, y - 200 + 2 * r + 20, x + 110, y - 200 + 2 * r + 50)
    rarm = (x + 140, y - 200 + 2 * r + 20, x + 170, y - 200 + 2 * r + 50)
    lleg = (x + 140, y - 200 + 2 * r + 80, x + 110, y - 200 + 2 * r + 110)
    rleg = (x + 140, y - 200 + 2 * r + 80, x + 170, y - 200 + 2 * r + 110)

    head = canvas.create_oval(head, width=width, state=tkinter.HIDDEN)
    torso = canvas.create_oval(torso, width=width, state=tkinter.HIDDEN)
    larm = canvas.create_line(larm, width=width, state=tkinter.HIDDEN)
    rarm = canvas.create_line(rarm, width=width, state=tkinter.HIDDEN)
    lleg = canvas.create_line(lleg, width=width, state=tkinter.HIDDEN)
    rleg = canvas.create_line(rleg, width=width, state=tkinter.HIDDEN)

    return head, torso, larm, rarm, lleg, rleg


def draw_letters(letters):
    start = width / 2 - 40 * len(letters)/2
    letter_ids = {letter:[] for letter in letters if letter != " "}
    for letter in letters:
        if letter == " ":
            start += 40
            continue
        canvas.create_line(start + 5, 100, start + 35, 100, width=2)
        idx = canvas.create_text(start + 20, 75, text=letter.upper(),
                                 font="arial 30", state=tkinter.HIDDEN)
        letter_ids[letter].append(idx)
        start += 40
    return letter_ids


draw_gallows(width / 2, height / 2 + 150)
hangman_ids = draw_hangman(width / 2, height / 2 + 150, 20)
ids = draw_letters("hello world")
print(ids)
canvas.mainloop()
