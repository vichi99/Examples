import random


def read():
    file = open("test.txt", "r")
    line = file.readline().rstrip()  # strip()
    while line:
        print(line)
        # print(repr(line))
        line = file.readline()
        if line == "\n":
            line = " "
            continue
        else:
            line = line.rstrip()
    file.close()


def read_easier():
    file = open("test.txt", "r")
    text = file.read()
    print(text)
    file.close()


def txt_with():
    with open("test.txt", "r") as file:
        for line in file:
            print(line.rstrip())


def write():
    file = open("test.txt", "w")  # a = append
    for i in range(10):
        random_n = random.randint(1, 10000)
        if i % 2 == 0:
            space = "\t"
        else:
            space = ""
        file.write("{}number {} => {}\n".format(space, i, random_n))
    file.close()
# Binary file is almost the same
# file= open("test.txt","rb"), we must add 'b' and we know what we want to read


# read()
# read_easier()
txt_with()
# write()
