#!/usr/bin/python3

"""
A class definition for a Student.
"""


class Student:
    """
    Defines a student with public instance attributes
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
        dict: The dictionary representation of the Student instance.
        """
        attributes = vars(self)
        serializable_attributes = {
            key: value for key, value in attributes.items()
            if isinstance(value, (str, int))
        }

        return serializable_attributes
