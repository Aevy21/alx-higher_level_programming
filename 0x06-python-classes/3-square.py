#!/usr/bin/python3
"""
    This class defines a square.
"""


class Square:
    """Represent a square.

    Attributes:
        __size (int): Private instance attribute \
                representing the size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square with an optional size.

        Args:
            size (int): Size of the square, validated as an integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
