#!/usr/bin/python3

"""
    Function that loads json to Python Objects.
"""


import json


def load_from_json_file(filename):
    """
        Function of load_from_json_file
        This function reads a json files and converts it
        into Python Objects.

        Args:
            filename (str): path to file.

        Retrun:
            the created Object.
    """

    with open(filename, "r") as file:
        # You can use this instead
        """
            # getting the file content
            content = file.read()
            # creating object form it
            obj = json.loads(content)
            # return the object
            return (obj)
        """
        return (json.load(file))
