##############################################################################
# The Hangman "Game"
##############################################################################
import tkinter
import random
import time
width, height = 640, 480

canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()

# GRAPHICS


def draw_gallows():
    x, y = width / 2, height / 2 + 150
    gnd = (x - 60, y, x + 60, y)
    frame = (x, y, x, y - 250,
             x, y - 250, x + 140, y - 250,
             x + 140, y - 250, x + 140, y - 200)
    canvas.create_line(gnd, width=10)
    canvas.create_line(frame, width=5)


def draw_hangman():
    x, y, r = width / 2, height / 2 + 150, 20
    width_man = 3
    head = (x + 140 - r, y - 200, x + 140 + r, y - 200 + 2 * r)
    torso = (x + 140, y - 200 + 2 * r, x + 140, y - 200 + 2 * r + 80)
    larm = (x + 140, y - 200 + 2 * r + 20, x + 110, y - 200 + 2 * r + 50)
    rarm = (x + 140, y - 200 + 2 * r + 20, x + 170, y - 200 + 2 * r + 50)
    lleg = (x + 140, y - 200 + 2 * r + 80, x + 110, y - 200 + 2 * r + 110)
    rleg = (x + 140, y - 200 + 2 * r + 80, x + 170, y - 200 + 2 * r + 110)

    head = canvas.create_oval(head, width=width_man, state=tkinter.HIDDEN)
    torso = canvas.create_oval(torso, width=width_man, state=tkinter.HIDDEN)
    larm = canvas.create_line(larm, width=width_man, state=tkinter.HIDDEN)
    rarm = canvas.create_line(rarm, width=width_man, state=tkinter.HIDDEN)
    lleg = canvas.create_line(lleg, width=width_man, state=tkinter.HIDDEN)
    rleg = canvas.create_line(rleg, width=width_man, state=tkinter.HIDDEN)

    return head, torso, larm, rarm, lleg, rleg


def draw_letters(letters):
    start = width / 2 - 40 * len(letters) / 2
    letter_ids = {letter: [] for letter in letters if letter != " "}
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


def update_letters(letter_ids, already_guessed):
    for letter, ids in letter_ids.items():
        if letter in already_guessed:
            for idx in ids:
                canvas.itemconfig(idx, state=tkinter.NORMAL)


def update_hangman(wrong_guesses, hangman_ids):
    for i in range(0, wrong_guesses):
        canvas.itemconfig(hangman_ids[i], state=tkinter.NORMAL)

# GAME LOGIC


def load_word():
    with open("data/words.txt", "r") as fp:
        word_list = fp.read().splitlines()
    random_word = random.choice(word_list)
    return random_word


def good_guess(letter):
    already_guessed.append(letter)
    update_letters(letter_ids, already_guessed)


def bad_guess(letter):
    global wrong_guesses
    already_guessed.append(letter)
    wrong_guesses += 1
    update_hangman(wrong_guesses, hangman_ids)


def is_winner(letter_ids, already_guessed):
    print("letter_ids {}".format(letter_ids))
    print("already {} ".format(already_guessed))
    for letter in letter_ids:
        print("letter {}".format(letter))
        if letter not in already_guessed:
            print("letter IF {}".format(letter))
            return False
    return True


def check_game_state():
    global game_state
    if is_winner(letter_ids, already_guessed):
        game_state = "WIN"
    elif wrong_guesses > 5:
        game_state = "LOSS"


def game_over(state):
    if state == "WIN":
        canvas.create_text(320, 240, text="NICE YOU WIN",
                           font="arial 60", fill="RED")
    else:
        canvas.create_text(320, 240, text="GAME OVER",
                           font="arial 60", fill="RED")
    canvas.update()
    time.sleep(3)


# INIT GLOBAL VARIABLES
draw_gallows()
hangman_ids = draw_hangman()
letter_ids = draw_letters(load_word())
game_state = "RUNNING"
already_guessed = []
wrong_guesses = 0

# MAIN LOOP
while game_state == "RUNNING":
    guess = input("guess letter: ")
    if guess in already_guessed:
        continue
    elif guess in letter_ids:
        good_guess(guess)
    else:
        bad_guess(guess)

    check_game_state()
    canvas.update()

game_over(game_state)
# canvas.mainloop()
