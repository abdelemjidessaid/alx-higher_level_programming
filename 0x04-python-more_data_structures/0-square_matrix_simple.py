#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    square = lambda x: x * x
    for i in matrix:
        result.append(list(map(square, i)))
    return (result)
