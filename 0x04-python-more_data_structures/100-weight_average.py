#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    mul = list(map((lambda item: item[0] * item[1]), my_list))
    div = list(map((lambda item: item[1]), my_list))
    s = sum(mul)
    d = sum(div)
    return (s / d)
