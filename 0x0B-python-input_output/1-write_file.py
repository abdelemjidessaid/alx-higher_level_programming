#!/usr/bin/python3

""" Function of write_file """


def write_file(filename="", text=""):
    """
        write_file - writes a text to text file.

        Args:
            filename (str): path to file.
            text (str): string that should be written.

        Return:
            number of bytes that is written.
    """

    # Open the filename in object named file
    with open(filename, "w", encoding="utf-8") as file:
        # Write the text and return the number of bytes written
        return (file.write(text))
