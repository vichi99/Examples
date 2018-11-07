import random

print("mastermind")

name = input("\nHi, whats your name ?: ")

print("""
So, {}
\rThe rules are the folowing. I mean a number and you'll be guessing (1-10).
If you want end the game,type 'end' .
On the end you will see yours score.\n\n""".format(name))
total, correct, incorrect = 0,0,0
while True:
    number = str(random.randint(1, 10))
    tip = input("\nI mean a number...\nYour tip?: ")

    if str.lower(str.strip(tip)) == "end":
        break
    elif tip == number:
        print("Correct !")
        correct += 1
    else:
        print("Incorrect ! Never mind.")
        incorrect += 1
    total += 1
print("correct: {} , incorrect: {} , total: {} ".format(correct,incorrect,total))
