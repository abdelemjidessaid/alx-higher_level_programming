#!/usr/bin/python3

""" Class Rectangle """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
            Method that calculates the area of rectangle.

            Return: width muliplied height.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
            Method that returns formated string.

            Return: formated string contains the info about rectangle.
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
