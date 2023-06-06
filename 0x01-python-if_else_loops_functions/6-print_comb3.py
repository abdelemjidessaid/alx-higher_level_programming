#!/usr/bin/python3

for i in range(10):
    for x in range(10):
        if i < x:
            print("{}{}".format(i, x), end="")
            print("{}".format("\n" if i == 8 and x == 9 else ", "), end="")
