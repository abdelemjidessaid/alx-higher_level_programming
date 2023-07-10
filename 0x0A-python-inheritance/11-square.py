#!/usr/bin/python3

""" Class Square """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        Class of Square that inherits from BaseGeomtry.
    """
    def __init__(self, size):
        """
            Constructor of Square

            Args:
                size (int): the size of square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            Method that calculates the area of square.

            Return: size muliplied by size.
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
            Method that returns formated string.

            Return: formated string contains the info about rectangle.
        """
        return (f"[Square] {self.__size}/{self.__size}")
