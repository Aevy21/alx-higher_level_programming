"""Unit test for class Base"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClassID(unittest.TestCase):
    """Tests the funtionality of class Base id assignment"""

    def test_id_none(self):
        """Tests for when @id is not initialized"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_positive_id(self):
        """Tests for when id is initialized with a postive int"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_zero_id(self):
        """Tests for when id is initialized to 0"""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_negative_id(self):
        """Tests for when id is initialized with a negative int"""
        b = Base(-15)
        self.assertEqual(b.id, -15)


class TestBaseClassToJSONString(unittest.TestCase):
    """Tests the functionality of class Base method to_json_string()"""

    def test_rectangle_1_list_dictionaries(self):
        """Tests to_json_string() with a list of dictionaries 
        on a Rectangle instance
        """
        rect = Rectangle(10, 7, 2, 8, 12)
        dictionary = rect.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        result_string =  '[{"id": 12, "width": 10, "height": 7, "x": 2, "y": 8}]'

        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, result_string)

    def test_square_1_list_dictionaries(self):
        """Tests to_json_string() with a list of dictionaries
        on a Square instance
        """
        sq = Square(10, 2, 8, 12)
        dictionary = sq.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        result_string =  '[{"id": 12, "size": 10, "x": 2, "y": 8}]'

        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, result_string)

    def test_2_list_dictionaries(self):
        """Tests a list with two dictionaries"""
        dict_list = [{'id': 13, 'x': 2}]
        dict_list.append({'id': 14, 'x': 3})
        json_dictionary = Base.to_json_string(dict_list)

        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, \
            '[{"id": 13, "x": 2}, {"id": 14, "x": 3}]')

    def test_None_list_dictionaries(self):
        """Tests to_json_string() when list_dictionaries is None"""
        json_dictionary = Base.to_json_string(None)
        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, "[]")

    def test_empty_list_dictionaries(self):
        """Tests to_json_string() when list_dictionaries=[]"""
        json_dictionary = Base.to_json_string([])
        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, "[]")


class TestBaseClassSaveToFile(unittest.TestCase):
    """Tests the functionality of the save_to_file() method"""

    @classmethod
    def tearDownClass(cls):
        """Deletes a file created after the class has run"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        if os.path.exists("Base.json"):
            os.remove("Base.json")

    def test_rectangle_instance_list(self):
        """Tests save_to_file() on a list of Rectangle instances"""
        rect = Rectangle(5, 10, 2, 2, 12)
        Rectangle.save_to_file([rect])

        file_content = '[{"id": 12, "width": 5, "height": 10, "x": 2, "y": 2}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), file_content)

    def test_empty_rectangle_instance_list(self):
        """Tests save_to_file() on an empty Rectangle class list"""
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_none_rectangle_instance_list(self):
        """Tests save_to_file() on Rectangle class when list_objs=None"""
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_square_instance_list(self):
        """Tests save_to_file() on a list of Square instances"""
        sq = Square(5, 2, 2, 13)
        Square.save_to_file([sq])

        file_content = '[{"id": 13, "size": 5, "x": 2, "y": 2}]'
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), file_content)

    def test_empty_square_instance_list(self):
        """Tests save_to_file() on an empty Square class list"""
        Square.save_to_file([])

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_none_square_instance_list(self):
        """Tests save_to_file() on Square class when list_objs=None"""
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")


class TestBaseClassFromJSONString(unittest.TestCase):
    """Tests the functionality of the from_json_string() method"""

    def test_rectangle_json_string(self):
        """Tests from_json_string() on a Rectangle instance"""
        list_input = [{"id": 12, "width": 10, "height": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertTrue(type(list_output), "<class 'list'>")
        self.assertEqual(list_output,  [{"id": 12, "width": 10, "height": 7}])

    def test_rectangle_empty_json_string(self):
        """Tests from_json_string() with json_string=''"""
        list_output = Rectangle.from_json_string("")
        self.assertEqual(list_output, [])

    def test_rectangle_none_json_string(self):
        """Tests from_json_string() with json_string=None"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_square_json_string(self):
        """Tests from_json_string() on a Square instance"""
        list_input = [{"id": 10, "size": 5}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)

        self.assertTrue(type(list_output), "<class 'list'>")
        self.assertEqual(list_output,  [{"id": 10, "size": 5}])

    def test_square_empty_json_string(self):
        """Tests from_json_string() with json_string=''"""
        list_output = Square.from_json_string("")
        self.assertEqual(list_output, [])

    def test_square_none_json_string(self):
        """Tests from_json_string() with json_string=None"""
        list_output = Square.from_json_string(None)
        self.assertEqual(list_output, [])


class TestBaseClassCreate(unittest.TestCase):
    """Tests the functionality of the create() method"""

    def test_rectangle_1_attribute_dict(self):
        """Tests create() on a Rectangle instance with dict of 1 attribute"""
        rect = Rectangle.create(**{"id": 10})
        self.assertEqual(str(rect), "[Rectangle] (10) 0/0 - 1/1")

    def test_rectangle_2_attributes_dict(self):
        """Tests create() on a Rectangle instance with dict of 2 attributes"""
        rect = Rectangle.create(**{"id": 10, "width": 5})
        self.assertEqual(str(rect), "[Rectangle] (10) 0/0 - 5/1")

    def test_rectangle_3_attributes_dict(self):
        """Tests create() on a Rectangle instance with dict of 3 attributes"""
        rect = Rectangle.create(**{"id": 10, "width": 5, "height": 10})
        self.assertEqual(str(rect), "[Rectangle] (10) 0/0 - 5/10")

    def test_rectangle_4_attributes_dict(self):
        """Tests create() on a Rectangle instance with dict of 4 attributes"""
        rect = Rectangle.create(**{"id": 10, "width": 5, "height": 10, "x": 2})
        self.assertEqual(str(rect), "[Rectangle] (10) 2/0 - 5/10")

    def test_rectangle_5_attributes_dict(self):
        """Tests create() on a Rectangle instance with dict of 5 attributes"""
        rect = Rectangle.create(**{"id": 10, "width": 5, "height": 10, "x": 2, "y": 2})
        self.assertEqual(str(rect), "[Rectangle] (10) 2/2 - 5/10")

    def test_square_1_attribute_dict(self):
        """Tests create() on a Square instance with dict of 1 attribute"""
        sq = Square.create(**{"id": 10})
        self.assertEqual(str(sq), "[Square] (10) 0/0 - 1")

    def test_square_2_attributes_dict(self):
        """Tests create() on a Square instance with dict of 2 attributes"""
        sq = Square.create(**{"id": 10, "size": 5})
        self.assertEqual(str(sq), "[Square] (10) 0/0 - 5")

    def test_square_3_attributes_dict(self):
        """Tests create() on a Square instance with dict of 3 attributes"""
        sq = Square.create(**{"id": 10, "size": 5, "x": 2})
        self.assertEqual(str(sq), "[Square] (10) 2/0 - 5")

    def test_square_4_attributes_dict(self):
        """Tests create() on a Square instance with dict of 4 attributes"""
        sq = Square.create(**{"id": 10, "size": 5, "x": 2, "y": 2})
        self.assertEqual(str(sq), "[Square] (10) 2/2 - 5")


class TestBaseClassLoadFromFile(unittest.TestCase):
    """Tests the functionality of the load_from_file() method"""

    @classmethod
    def tearDownClass(cls):
        """Deletes a file created after the class has run"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        if os.path.exists("Base.json"):
            os.remove("Base.json")

    def test_rectangle_class_load(self):
        """Tests load_from_file() with Rectangle class"""
        rect = Rectangle(5, 10, 2, 2, 12)
        Rectangle.save_to_file([rect])
        list_rect = Rectangle.load_from_file()
        new_rect = list_rect[0]

        self.assertFalse(rect is new_rect)
        self.assertEqual(str(new_rect), "[Rectangle] (12) 2/2 - 5/10")

    def test_rectangle_inexistent_file(self):
        """Tests load_from_file() with an inexistent file"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        list_rect = Rectangle.load_from_file()
        self.assertEqual(list_rect, [])

    def test_square_class_load(self):
        """Tests load_from_file() with Square class"""
        sq = Square(5, 2, 2, 12)
        Square.save_to_file([sq])
        list_sq = Square.load_from_file()
        new_sq = list_sq[0]

        self.assertFalse(sq is new_sq)
        self.assertEqual(str(new_sq), "[Square] (12) 2/2 - 5")

    def test_square_inexistent_file(self):
        """Tests load_from_file() with an inexistent file"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        list_sq = Square.load_from_file()
        self.assertEqual(list_sq, [])
