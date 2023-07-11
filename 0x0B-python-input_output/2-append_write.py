#!/usr/bin/python3

"""Function of append_write"""


def append_write(filename="", text=""):
    """
        append_write - function that appending a text to the end of
        a given file, and returns the number of bytes that is written.

        Args:
            filename (str): path of file.
            text (str): the text tha should be written.
        Return:
            number of bytes that is written.
    """

    # Open filename in obj named file
    with open(filename, "a", encoding="utf-8") as file:
        # Write the text content.
        bytes = file.write(text)
        # Return the number of bytes.
        """
            You can use next
            return (file.write(text))

            Instead of this
            bytes = file.write(text)
            return (bytes)
        """
        return (bytes)
