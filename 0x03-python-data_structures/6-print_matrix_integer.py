#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    out = len(matrix)
    for x in range(out):
        i = len(matrix[x])
        for y in range(i):
            if y < i - 1:
                print("{:d}".format(matrix[x][y]), end=" ")
            else:
                print("{:d}".format(matrix[x][y]))
