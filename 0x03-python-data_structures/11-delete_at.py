#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    ln = len(my_list)
    if ln < 0 or idx > ln - 1:
        return (my_list)
    del my_list[idx]
    return (my_list)
