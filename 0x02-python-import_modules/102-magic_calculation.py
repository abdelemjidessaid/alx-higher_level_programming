#!/usr/bin/python3
import magic_calculation_102 as magic


def magic_calculation(a, b):
    if a < b:
        c = magic.add(a, b)
        for i in range(4, 6):
            c = magic.add(c, i)
        return (c)
    else:
        return magic.sub(a, b)
