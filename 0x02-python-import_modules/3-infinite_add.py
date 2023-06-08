#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as ar
    size = len(ar)
    sum = 0
    for i in range(1, size):
        sum += int(ar[i])
    print("{:d}".format(sum))
