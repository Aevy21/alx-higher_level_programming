#!/usr/bin/python3
"""
Note:
    Prints a square of a specified size using the character '#'.

"""
def print_square(size):
    """
    Prints a square of a specified size using the character '#'.

    Parameters:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer or if size is a float and less than 0.
    - ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is a float and is less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    for _ in range(size):
        print("#" * size)
