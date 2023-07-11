#!/usr/bin/python3

"""
    Function that returns the pascal's triangle.
"""


def pascal_triangle(n):
    """
        Function that returns a list of lists of integers
        of triangle.

        Args:
            n (int): number of lists and digits

        Returns:
            list of lists
    """
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
