#!/usr/bin/python3
"""
Note: This  function magic_string() that returns a \
        string “BestSchool” n times the number of the iteration

"""


def magic_string(n):
    """
    Generate a string by concatenating "BestSchool" repeated \
            n times based on iteration number.

    Args:
        n (int): Number of iterations.

    Returns:
        str: The generated string.
    """
    result = ""
    for i in range(1, n + 1):
        part = "BestSchool" * i
        # Create a substring "BestSchool" repeated i times
        result += part
        # Append the substring to the result string
    return result
