#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    out = len(matrix)
    for x in range(out):
        i = len(matrix[x])
        for y in range(i):
            if y < i - 1:
                print("{}".format(matrix[x][y]), end=" ")
            else:
                print("{}".format(matrix[x][y]))
