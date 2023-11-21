#!/usr/bin/python3
"""
Note:
        This class is a basic representation of a square \
                and does not handle specific functionalities.
    """


class Square:
    """
    This class defines a square.
    """
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("Size must be an integer")

            if size < 0:
                raise ValueError("Size must be >= 0")

            self.__size = size
        except (TypeError, ValueError) as e:
            print(f"{e}")
