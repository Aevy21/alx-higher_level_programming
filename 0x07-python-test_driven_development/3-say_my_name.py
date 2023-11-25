#!/usr/bin/python3

"""
Note  This function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
   """
    Parameters:
    - first_name (str): The first name.
    - last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
    - TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    
    full_name = "My name is {} {}".format(first_name, last_name)
    print(full_name)
