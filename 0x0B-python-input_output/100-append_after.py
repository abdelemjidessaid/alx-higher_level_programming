#!/usr/bin/python3

"""
    Module for append_after method.
"""


def append_after(filename="", search_string="", new_string=""):
    """
        Function that adds a string in a specific position
        in a file.

        Args:
            filename (str): the file path.
            search_string (str): the keyword to search for.
            new_string (str): the string that should insert.
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines[i:i + 1] = [lines[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
