#!/usr/bin/python3

string = ""

for i in range(97, 123):
    if i == 113 or i == 101:
        continue
    string += chr(i)
print("{}".format(string), end="")
