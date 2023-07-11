#!/usr/bin/python3

"""Function of read_file"""


def read_file(filename=""):
    """
        Function that a text file with UTF-8 Encoding and prints it out
        to the `stdout`

        Args:
            filename (str): path of file.
    """
    if (filename == ""):
        return
    with open(filename, "r", encoding="utf-8") as file:
        for i in file:
            print(i)
