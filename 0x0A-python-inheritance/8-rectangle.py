#!/usr/bin/python3


BaseGeometry = __import__("7-base_geometry").BaseGeometry


"""Class Rectangle"""


class Rectangle(BaseGeometry):
    """
        Class Rectangle that inherits from BaseGreometry
    """
    def __init__(self, width, height):
        """
            Constructor of Rectangle's Class.

            Args:
                width (int): number of width.
                height (int): number of height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
