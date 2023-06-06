#!/usr/bin/python3

def uppercase(str):
    for i in str:
        code = ord(i)
        char = chr(code - 32) if code in range(97, 123) else i
        print("{}".format(char), end="")
    print("")
