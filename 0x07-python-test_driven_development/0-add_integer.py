#!/usr/bin/python3
"""
Note: This function only adds integers and typecasted floats.
"""

def add_integer(a, b=98):
    """
    Adds two numbers and returns the result as an integer.
    
    Parameters:
    :param a: First number (integer or float).
    :param b: Second number (integer or float, default is 98).
    
    Returns:
    :return: The sum of a and b, casted to an integer.
    """
    
    # Check if both a and b are either integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Cast a and b to integers and return their sum
    return int(a) + int(b)

