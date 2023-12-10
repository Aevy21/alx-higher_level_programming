#!/usr/bin/python3
"""
a Base with a private class attr
"""


import json


class Base:
    """

    Attributes:
    __nb_objects (int): Private class attr to keep track of the num of objects.
    id (int): Public instance attr representing the object's ID.
    """

    __nb_objects = 0  # private class attr

    def __init__(self, id=None):
        """
        Args:
            id (int, optional): If provided, assigns the given ID. \
                    If None, auto-increments the ID.

        Note:
            If id is not provided, it will be auto generated\
                    using the __nb_objects counter.
        """
        if id is not None:
            self.id = id  # assign id if provided
        else:
            Base.__nb_objects += 1  # increment class attr
            self.id = Base.__nb_objects  # assign the new value to id
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        file_name = "{}.json".format(class_name)

        # Create a list of dictionaries representing each object
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Convert the list of dictionaries to a JSON string
        json_string = cls.to_json_string(list_dicts)

        # Write the JSON string to a file, overwriting if it already exists
        with open(file_name, 'w') as file:
            file.write(json_string)

    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square
        else:
            raise ValueError("Unsupported class for create method")

        # Call update method to apply real values
        dummy_instance.update(**dictionary)
        return dummy_instance


    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a file.

        Returns:
            list: List of instances.
        """
        class_name = cls.__name__
        file_name = "{}.json".format(class_name)

        try:
            with open(file_name, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**obj_dict) for obj_dict in list_dicts]
