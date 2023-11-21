#!/usr/bin/python3
"""
    This class defines a square.
"""


class Square:
    """Define a square.

    Attributes:
        __size (int): Private instance attribute \
                representing the size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square with optional size.

        Args:
            size (int): Size of the square, validated as an integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): Size of the square, validated as an integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

def my_print(self):
        """
        Prints a representation of the square using the '#' character.

        If the size of the square is 0, an empty line is printed instead.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.size):
            for _ in range(self.size):
                print("#", end="")
            print()
