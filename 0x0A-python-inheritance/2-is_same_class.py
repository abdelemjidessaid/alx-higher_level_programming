#!/usr/bin/python3

"""Function of is_same_class"""


def is_same_class(obj, a_class):
    """
    is_same_class Function that returns `True` if obj issubclass of a_class
    """
    return (type(obj) == a_class)
