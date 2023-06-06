#!/usr/bin/bash

for i in range(100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{}{}, ".format("" if i < 10 else "0", i), end="")
