#!/usr/bin/python3

def uniq_add(my_list=[]):
    l = []
    result = 0
    for i in my_list:
        if i not in l:
            l.append(i)
            result += i
    return (result)
