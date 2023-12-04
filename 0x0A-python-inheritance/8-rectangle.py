#!/usr/bin/python3

"""
definition of a class named Rectangle that inherits from BaseGeometry
"""

class BaseGeometry:
    """A class with area and integer_validator methods."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value.

        Parameters:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{name} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{name} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry for representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height.

        Parameters:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
