#!/usr/bin/python3

""" Class of MyList """


class MyList(list):
    """
    MyList class that contains a method print_sorted that prints
        lists but sorted ascendind sort.
    """

    def __init__(self):
        """Inherit from the base class of list."""
        super().__init__()

    def print_sorted(self):
        """
        print_sorted prints lists but sorted ascending sort.

        Args: None.

        Return: None.
        """
        print(sorted(self))
