#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    res = ()
    for i in range(2):
        sum = 0
        if len(tuple_a) - 1 >= i:
            sum += tuple_a[i]
        if len(tuple_b) - 1 >= i:
            sum += tuple_b[i]
        res = res + (sum,)
    return (res)
