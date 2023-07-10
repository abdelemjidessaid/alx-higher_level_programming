#!/usr/bin/python3

"""
Function that checks the object if it is instances of class that inherited.
"""


def inherits_from(obj, a_class):
    """
        Function that checks the object if it is
        instances of class that inherited.

        Args:
            obj (instance): instance of a class.
            a_class (class): class name.

        Return: True if the obj is instance of a class inherited,
        False otherwise.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
