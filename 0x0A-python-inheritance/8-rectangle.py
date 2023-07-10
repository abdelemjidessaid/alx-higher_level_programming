#!/usr/bin/python3

"""Class of BaseGeometry"""


class BaseGeometry:
    """
        class of BaseGeometry
        is an empty class.
    """
    def area(self):
        """
            Constructor of BaseGeometry
            Raises an Exception when an instance is created.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Function that validate name and value.

            Args:
                name (str): conntains a name.
                value (int): contains a number.
        """
        if (not isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")


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
