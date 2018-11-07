import random

print("""___  ___          _           ___  ____           _
|  \/  |         | |          |  \/  (_)         | |
| .  . | __ _ ___| |_ ___ _ __| .  . |_ _ __   __| |
| |\/| |/ _` / __| __/ _ \ '__| |\/| | | '_ \ / _` |
| |  | | (_| \__ \ ||  __/ |  | |  | | | | | | (_| |
\_|  |_/\__,_|___/\__\___|_|  \_|  |_/_|_| |_|\__,_|
""")


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


print("""
\r+{0:-^20}+
\r| {1:{width}} | {2:{width_n}} |
\r| {3:{width}} | {4:{width_n}} |
\r| {5:{width}} | {6:{width_n}} |
\r+{7:-^20}+""".format("Your Score","Correct",correct, "Incorrect", incorrect, "Total", total,"", width = 10,width_n=5))
