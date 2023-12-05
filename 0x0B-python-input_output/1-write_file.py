#!/usr/bin/python3
"""
This function writes a string to a text file (UTF-8) and returns the
number of characters written.
"""


def write_file(filename="", text=""):
    """This function writes a string to a text file (UTF-8) and returns the
    number of characters written.

    Parameters:
    - filename (str, optional): The name of the file to be written.
      Default is an empty string.
    - text (str): The string to be written to the file.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return (file.write(text))
