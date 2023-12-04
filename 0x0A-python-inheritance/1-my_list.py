#!/usr/bin/python3

"""
a class MyList that inherits from list
"""


class MyList(list):
    """A custom list class inheriting from the built-in list class."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
