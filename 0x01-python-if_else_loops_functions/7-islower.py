#!/usr/bin/python3

def islower(c):
    if c == '':
        return (False)
    code = ord(c)
    return (code >= 97 and code <= 122)
