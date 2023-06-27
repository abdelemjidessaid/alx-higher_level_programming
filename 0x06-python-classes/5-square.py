#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """This is getter, returns the current rib's size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """this method prints the square with next character '#'."""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
