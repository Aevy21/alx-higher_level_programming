#!/usr/bin/python3
"""
Note: This function only adds integers and typecasted floats.
Returns:
    :return: The sum o a and b ,casted to an integer
"""


def add_integer(a, b=98):
    """
    parameter a: First number (integer or float).\
            param b: Second number (integer or float, default is 98).
    """

    # Check if both a and b are either integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Cast a and b to integers and return their sum
    return int(a) + int(b)
