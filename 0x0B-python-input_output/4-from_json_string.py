#!/usr/bin/python3

""" Function of from_json_string """


import json


def from_json_string(my_str):
    """
        from_json_string - function that creates python objects
        from JSON strings and returns it.

        Args:
            my_str (str): the target string.
        Return:
            the object that is created.
    """

    return (json.loads(my_str))
