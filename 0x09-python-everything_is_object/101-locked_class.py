#!/usr/bin/python3

"""This is the class of LockedClass"""


class LockedClass:
    """
    This class prevents creating new instances except
    instance named 'first_name'.
    """

    __slots__ = ["first_name"]
