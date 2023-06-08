#!/usr/bin/python3
from sys import argv as ar

length = len(ar)
status = ""
if length == 1:
    status = "s."
elif length == 2:
    status = ":"
else:
    status = "s:"
print("{} argument{}".format(length - 1, status))
if length > 1:
    for i in range(1, len(ar)):
        print("{}: {}".format(i, ar[i]))
