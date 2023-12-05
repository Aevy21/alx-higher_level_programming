#!/usr/bin/python3
"""
Read File Function:
This function reads the content of a text file (UTF-8) and prints it to stdout.
"""


def read_file(filename=""):
    """This function reads the content of a text file (UTF-8) and \
            prints it to stdout.

    Parameters:
    - filename (str, optional): The name of the file to be read.\
            Default is an empty string.

    Returns:
    None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
