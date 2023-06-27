#!/usr/bin/python3

"""Represent Square as python class"""


class Square:
    """Task 2, class Square that defines a square by: (based on 1-square.py)"""
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
