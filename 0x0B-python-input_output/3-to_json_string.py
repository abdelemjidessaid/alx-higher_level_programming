#!/usr/bin/python3

""" Function of to_json_string """


import json

def to_json_string(my_obj):
    """
        to_json_string - function that returns object as JSON.

        Args:
            my_obj (object): the object that should be converted.
        Return:
            string contains json of my_obj
    """

    return (json.dumps(my_obj))
