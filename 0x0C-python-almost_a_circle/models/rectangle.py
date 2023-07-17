#!/usr/bin/python3

""" The rectangle module """
from .base import Base


class Rectangle(Base):
    """
        The class Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            The constructor of Rectangle class.

            Args:
                width (int): the width variable.
                height (int): the height variable.
                x (int): x axis.
                y (int): y axis.
                id (int): the id of each instance.
        """

        super().__init__(id)
        self.validateType("width", width)
        self.validateValue("width", width)
        self.__width = width
        self.validateType("height", height)
        self.validateValue("width", height)
        self.__height = height
        self.validateValue("x", x)
        self.__x = x
        self.validateValue("y", y)
        self.__y = y

    def __str__(self):
        """
            Function that returns the rectangle info for the print function.

            Return:
                formated string that contains the rectangle's info.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def validateType(self, name, value):
        """
            Function that validate the type of attributes.
            If the type is not integer raises a TypeError.

            Args:
                name (str): the name of attribute.
                value (int): the value of attribute.
        """
        if (type(value) != int):
            raise TypeError(f"{name} must be an integer")

    def validateValue(self, name, value):
        """
            Function that validates the value of width, height, x and y.
            If the value is less or equal to 0 raises a ValueError

            Args:
                name (str): the name of attribute.
                value (int): the value of the attr.
        """
        if (name == "x" or name == "y"):
            if (value < 0):
                raise ValueError(f"{name} must be >= 0")
        else:
            if (value <= 0):
                raise ValueError(f"{name} must be > 0")

    def area(self):
        """
            Function that returns the area of the rectangle.

            Return:
                a number which is the rectangle's area.
        """
        return (self.__width * self.__height)

    def display(self):
        """
            Function that prints the rectangle with symbols like #.
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
            Function that updates all attributes in one time.

            Args:
                args (list): list of attribute values.
                kwargs (dict): dictionary of attribute
                    names and its values.
        """
        if args:
            i = 0
            while (i < len(args)):
                if (i == 0):
                    super().__init__(args[i])
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                else:
                    self.__y = args[i]
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Function that returns the attributes in dictionary.

            Return:
                dictionary that contains all attribute's
                names and its values.
        """
        return (
            {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }
        )

    @property
    def width(self):
        """
            Getter of width attribute.

            Return:
                the width value.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
            Setter of width attribute.

            Args:
                value (int): the new value of width.
        """
        self.validateType("width", value)
        self.validateValue("width", value)
        self.__width = value

    @property
    def height(self):
        """
            Getter of the height attribute.

            Return:
                the value of height attribute.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
            Setter of the height attribute.

            Args:
                value (int): the new value of height.
        """
        self.validateType("height", value)
        self.validateValue("height", value)
        self.__height = value

    @property
    def x(self):
        """
            Getter of the x attribute.

            Return:
                the value of x attribute.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
            Setter of the x attribute.

            Args:
                value (int): the new value of x attribute.
        """
        self.validateType("x", value)
        self.validateValue("x", value)
        self.__x = value

    @property
    def y(self):
        """
            Getter of the y attribute.

            Return:
                the value of y attribute.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
            Setter of the y attribute.

            Args:
                value (int): the new value of y attr.
        """
        self.validateType("y", value)
        self.validateValue("y", value)
        self.__y = value
