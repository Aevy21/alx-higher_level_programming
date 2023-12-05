#!/usr/bin/python3

"""
A class definition for a Student.
"""


class Student:
    """
    Defines a student with public instance attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name, and age.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs (list, optional): If a list of strings, only attribute names
          contained in this list must be retrieved. Otherwise, all attributes
          must be retrieved.

        Returns:
        dict: The dict representation of the Student instance.
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            return vars(self)

    def reload_from_json(self, json):
        """
        Replaces all attr of the Student instance with values from a dict.

        Parameters:
        - json (dict): A dict where keys are attribute names and values are
          the new values for the corresponding attr.

        Returns:
        None
        """
        for key, value in json.items():
            setattr(self, key, value)
