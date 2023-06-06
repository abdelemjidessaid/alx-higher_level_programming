#!/usr/bin/python3

def islower(c):
    if c == '':
        return (None)
    code = ord(c)
    return (code >= 97 and code <= 122)
