#!/usr/bin/python3

""" The square module """
from .rectangle import Rectangle


class Square(Rectangle):
    """
        The class of Square that is inherit from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            The constructor of Square class.

            Args:
                size (int): the size of ribs.
                x (int): the x position.
                y (int): the y position.
                id (int): the instance id.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
            Function that returns a formated string that contains
            the Square info.

            Return:
                Formated string contains all Square info.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
            Getter of size attribute.

            Return:
                the size's value.
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
            Setter of size attribute.

            Args:
                value (int): the new value of size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Function that updates the instance's attributes.

            Args:
                args (list): list of attribute's values.
                kwargs (dict): dictionary of attribute's values.
        """
        if args:
            for i in range(len(args)):
                if (i == 0):
                    self.id = args[i]
                if (i == 1):
                    self.size = args[i]
                if (i == 2):
                    self.x = args[i]
                if (i == 3):
                    self.y = args[i]
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
                "size": self.size,
                "x": self.x,
                "y": self.y
            }
        )
