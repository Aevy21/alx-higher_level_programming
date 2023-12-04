#!/usr/bin/python3

"""
A rebellious integer class, MyInt, that inherits from the built-in int class
"""


class MyInt(int):
    """
    A class representing an integer with inverted equality operators.

    Attributes:
        value (int): The integer value.
    """

    def __init__(self, value):
        """
        Initializes a MyInt instance.

        Args:
            value (int): The integer value.
        """
        self.value = value

    def __eq__(self, other):
        """
        Inverts the equality operator.

        Args:
            other (int): The other integer for comparison.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the inequality operator.

        Args:
            other (int): The other integer for comparison.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
