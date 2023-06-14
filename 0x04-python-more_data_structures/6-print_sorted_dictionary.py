#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    order = sorted(a_dictionary)
    for k in order:
        print("{}: {}".format(k, a_dictionary[k]))
