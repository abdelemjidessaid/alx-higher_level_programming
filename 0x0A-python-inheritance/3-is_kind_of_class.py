#!/usr/bin/python3

"""
Function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
        unction that returns True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False

        Args:
            obj (instance): object of a class.
            a_class (class): class name.
        Return:
            True if the object is an instance of a_classor
            or if the object is an instance of a class that inherited from,
            False otherwise.
    """
    if (isinstance(obj, a_class) or issubclass(type(obj), a_class)):
        return (True)
    else:
        return (False)
