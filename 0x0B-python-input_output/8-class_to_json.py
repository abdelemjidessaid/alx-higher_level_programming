#!/usr/bin/python3

"""
    Function that converts objects to json
"""


def class_to_json(obj):
    """
        class_to_json - function that converts python objects to json.

        Args:
            obj (object): object of a class.

        Return:
            the json code that is created from obj.
    """

    return (obj.__dict__)
