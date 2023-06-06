#!/usr/bin/python3

def uppercase(str):
    for i in str:
        code = ord(i)
        print("{}".format(chr(code - 32) if code in range(97, 123) else i), end="")
    print("")
