#!/usr/bin/python3

"""
This module defines a class called `Square` that represents a square.

Args:
    size: The size of the square. \
            Must be an integer greater than or equal to 0.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        size: The size of the square. An integer greater than or equal to 0.
    """

    def __init__(self, size=0):
        """
        Constructs a new `Square` object.
        Args:
            size: The size of the square. Must be \
                    an integer greater than or equal to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            An integer representing the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value: The new size of the square. \
                    Must be an integer greater than or equal to 0.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            An integer representing the area of the square.
        """
        return int(self.__size) ** 2

    def my_print(self):
        """
        Prints the square to the standard output stream.

        If the size of the square is 0, nothing is printed.\
                Otherwise, the square is printed
        using the '#' character.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print('#' * self.__size)
