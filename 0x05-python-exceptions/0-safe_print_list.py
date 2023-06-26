#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            counter += 1
        print("")
    except:
        print("")
        return (counter)
    return (counter)

if (__name__ == "__main"):
        safe_print_list()
