#!/usr/bin/python3

"""Function of is_same_class"""


def is_same_class(obj, a_class):
    """
    is_same_class Function that returns `True` if obj issubclass of a_class
    """
    if (obj is None or a_class is None):
        return (False)
    if (a_class == object):
        return (False)
    return (isinstance(obj, a_class))
