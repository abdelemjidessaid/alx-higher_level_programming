#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list == None:
        return (None)
    copy = my_list.copy()
    if idx < 0 or idx > len(copy) - 1:
        return (copy)
    else:
        copy[idx] = element
        return (copy)
