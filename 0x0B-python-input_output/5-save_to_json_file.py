#!/usr/bin/python3

"""
    Function of 
"""


import json


def save_to_json_file(my_obj, filename):
    """
        Function of save_to_json_file that creates a file contains
        JSON content, that is creates from a given Python Object.

        Args:
            my_obj (Object): the object that should be converted.
            filename (str): the file path.
    """

    # Write the json code to the filename.
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
