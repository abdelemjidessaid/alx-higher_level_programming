#!/usr/bin/python3

def no_c(my_string):
    if my_string != None:
        copy = ""
        for i in my_string:
            if i != "c" and i != "C":
                copy += i
        return (copy)
    return (None)