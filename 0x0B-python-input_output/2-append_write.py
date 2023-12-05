#!/usr/bin/python3
"""
This function appends a string to the end of a text file (UTF-8) and
returns the number of characters added.
"""


def append_write(filename="", text=""):
    """This function appends a string to the end of a text file (UTF-8) and
    returns the number of characters added.

    Parameters:
    - filename (str, optional): The name of the file to be appended.
      Default is an empty string.
    - text (str): The string to be appended to the file.

    Returns:
    int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
