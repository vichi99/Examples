##############################################################################
# The program shows how works reading and writing for a txt and csv file
##############################################################################

import random
import csv


def txt_read():
    file = open("data/test.txt", "r")
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


def txt_read_easier():
    file = open("data/test.txt", "r")
    text = file.read()
    print(text)
    file.close()


def txt_with():
    with open("data/test.txt", "r") as file:
        for line in file:
            print(line.rstrip())


def txt_write():
    file = open("data/test.txt", "w")  # a = append
    for i in range(10):
        random_n = random.randint(1, 10000)
        if i % 2 == 0:
            space = "\t"
        else:
            space = ""
        file.write("{}number, {} =>, {}\n".format(space, i, random_n))
    file.close()
# Binary file is almost the same
# file= open("test.txt","rb"), we must add 'b' and we know what we want to read


def txt_read_del():
    delimiter = ","
    tab = []
    with open("data/movies.csv", "r") as file:
        for line in file:
            line = line.rstrip()
            tab.append(line.split(delimiter))
    print(tab)


def csv_read():
    tab = []
    with open("data/movies.csv", "r") as file:
        r = csv.reader(file)
        for line in r:
            print(line)

# def csv_read():
#     tab = []
#     with open("data.csv","r") as file:
#         r=csv.DictReader(file)
#         for line in r:
#             print("{:.<60} {}".format(line["Title"],line["Rating"]))


def csv_dict():
    tab = []
    with open("data/movies.csv", "r") as file:
        r = csv.DictReader(file)
        for line in r:
            tab.append(line)
        print(line)



# txt_read()
# txt_read_easier()
# txt_with()
# txt_write()
# txt_read_del()
csv_read()
# csv_dict()
