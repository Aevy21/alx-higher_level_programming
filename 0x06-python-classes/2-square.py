#!/usr/bin/python3
"""
    This class defines a square.
    """


class Square:
    """Represent a square.

    Attributes:
        __size (int):Private instance attribute
    """

    def __init__(self, size=0):
        """Initialize a new Square with optional size.

        Args:
            size ,size being an int value which is bing validated
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
