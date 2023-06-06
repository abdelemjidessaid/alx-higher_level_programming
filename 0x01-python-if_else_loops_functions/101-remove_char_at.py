#!/usr/bin/python3

def remove_char_at(str, n):
    counter = 0
    tmp = ""
    for i in str:
        if counter == n:
            counter += 1
            continue
        tmp += i
        counter += 1
    return (tmp)
