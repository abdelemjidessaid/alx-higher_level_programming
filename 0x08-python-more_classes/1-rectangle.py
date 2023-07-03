#!/usr/bin/python3

"""Class Rectangle is an empty class."""


class Rectangle:
    """Rectangle is a class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """As constructure that initializes the attributes.
            Args:
                width (int): initializing the width variable.
                height (int): initializing the height variable.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This is a getter method, that retrieves the value of width
            Return:
                width (int): the value in width var.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """This is a setter method that sets a new value to width var.
            Args:
                width (int): new value that should sets to width var.
            Return: None.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if (width < 0):
            ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """This is a getter method, that retrieves the value of height
            Return:
                height (int): the value in width var.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """This is a setter method that sets a new value to height var.
            Args:
                height (int): new value that should sets to height var.
            Return: None.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if (height < 0):
            ValueError("height must be >= 0")
        self.__height = height
