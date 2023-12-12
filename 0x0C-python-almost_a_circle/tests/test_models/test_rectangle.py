""" Unit test for class Rectangle """

import unittest
from models.rectangle import Rectangle


class TestRectangleClassInstantiation(unittest.TestCase):
    """Tests variations of class Rectangle instantiation"""

    def test_normal_Rectangle(self):
        """Proper object instantiation with integer width and

        height args > 0
        """
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(6, 12)

        self.assertEqual(rect2.id, rect1.id + 1)
        self.assertEqual(rect1.width, 5)
        self.assertEqual(rect1.height, 10)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

    def test_unique_id(self):
        """Proper object instantiation with integer width and

        height args > 0, and unique id
        """
        rect1 = Rectangle(4, 8)
        rect2 = Rectangle(5, 10, id=12)
        rect3 = Rectangle(6, 12)

        self.assertEqual(rect2.id, 12)
        self.assertEqual(rect3.id, rect1.id + 1)

    def test_unique_x(self):
        """Object instantiation with int x value >= 0"""
        rect1 = Rectangle(5, 10, x=1)
        rect2 = Rectangle(6, 12, x=15)

        self.assertEqual(rect1.x, 1)
        self.assertEqual(rect2.x, 15)

    def test_negative_x(self):
        """Object instantiation with int x value < 0"""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, x=-5)

    def test_string_x(self):
        """Object instantiation with x of type str"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "5")

    def test_list_x(self):
        """Object instantiation with x of type list"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, [5])

    def test_tuple_x(self):
        """Object instantiation with x of type tuple"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, (5, ))

    def test_set_x(self):
        """Object instantiation with x of type set"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, {3, 4})

    def test_dictionary_x(self):
        """Object instantiation with x of type dict"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, {"x": 5})

    def test_unique_y(self):
        """Object instantiation with int y value >= 0"""
        rect1 = Rectangle(5, 10, y=1)
        rect2 = Rectangle(6, 12, y=15)

        self.assertEqual(rect1.y, 1)
        self.assertEqual(rect2.y, 15)

    def test_negative_y(self):
        """Object instantiation with int y value < 0"""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, y=-5)

    def test_string_y(self):
        """Object instantiation with y of type str"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "5")

    def test_list_y(self):
        """Object instantiation with y of type list"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, [5])

    def test_tuple_y(self):
        """Object instantiation with y of type tuple"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, (5, ))

    def test_set_y(self):
        """Object instantiation with y of type set"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, {3, 4})

    def test_dictionary_y(self):
        """Object instantiation with y of type dict"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, {"y": 5})

    def test_zero_width(self):
        """Instantiating Rectangle class with width = 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10)

    def test_negative_width(self):
        """Instantiating Rectangle class with width < 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_string_width(self):
        """Object instantiation with width of type str"""
        with self.assertRaises(TypeError):
            Rectangle("5", 10)

    def test_list_width(self):
        """Object instantiation with width of type list"""
        with self.assertRaises(TypeError):
            Rectangle([5], 10)

    def test_tuple_width(self):
        """Object instantiation with width of type tuple"""
        with self.assertRaises(TypeError):
            Rectangle((5, ), 10)

    def test_set_width(self):
        """Object instantiation with width of type set"""
        with self.assertRaises(TypeError):
            Rectangle({5}, 10)

    def test_dictionary_width(self):
        """Object instantiation with width of type dict"""
        with self.assertRaises(TypeError):
            Rectangle({"width": 5}, 10)

    def test_zero_height(self):
        """Instantiating Rectangle class with height = 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 0)

    def test_negative_height(self):
        """Instantiating Rectangle class with height < 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

    def test_string_height(self):
        """Object instantiation with height of type str"""
        with self.assertRaises(TypeError):
            Rectangle(5, "10")

    def test_list_height(self):
        """Object instantiation with height of type list"""
        with self.assertRaises(TypeError):
            Rectangle(5, [10])

    def test_tuple_height(self):
        """Object instantiation with height of type tuple"""
        with self.assertRaises(TypeError):
            Rectangle(5, (10, ))

    def test_set_height(self):
        """Object instantiation with height of type set"""
        with self.assertRaises(TypeError):
            Rectangle(5, {10})

    def test_dictionary_height(self):
        """Object instantiation with height of type dict"""
        with self.assertRaises(TypeError):
            Rectangle(5, {"height": 10})


class TestRectangleSetters(unittest.TestCase):
    """Tests the functionality of Rectangle attribute setters"""

    def test_width_setter(self):
        """Sets width of a Rectangle instance to an int > 0"""
        rect = Rectangle(5, 10)
        rect.width = 12
        self.assertEqual(rect.width, 12)

    def test_zero_width_setter(self):
        """Attempts to set width to an int = 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10)
            rect.width = 0

    def test_negative_width_setter(self):
        """Attempts to set width to an int < 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10)
            rect.width = -5

    def test_string_width_setter(self):
        """Attempts to set width of type str"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.width = "6"

    def test_list_width_setter(self):
        """Attempts to set width of type list"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.width = [6]

    def test_tuple_width_setter(self):
        """Attempts to set width of type tuple"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.width = (6, )

    def test_set_width_setter(self):
        """Attempts to set width of type set"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.width = {6}

    def test_dictionary_width_setter(self):
        """Attempts to set width of type dict"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.width = {"width": 6}

    def test_height_setter(self):
        """Sets height of a Rectangle instance to an int > 0"""
        rect = Rectangle(5, 10)
        rect.height = 6
        self.assertEqual(rect.height, 6)

    def test_zero_height_setter(self):
        """Attempts to set height to an int = 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10)
            rect.height = 0

    def test_negative_height_setter(self):
        """Attempts to set height to an int < 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10)
            rect.height = -10

    def test_string_height_setter(self):
        """Attempts to set height of type str"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.height = "12"

    def test_list_height_setter(self):
        """Attempts to set height of type list"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.height = [12]

    def test_tuple_height_setter(self):
        """Attempts to set height of type tuple"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.height = (12, )

    def test_set_height_setter(self):
        """Attempts to set height of type set"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.height = {12}

    def test_dictionary_height_setter(self):
        """Attempts to set height of type dict"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.height = {"height": 12}

    def test_zero_x_setter(self):
        """Attempts to set x to an int = 0"""
        rect = Rectangle(5, 10)
        rect.x = 0
        self.assertEqual(rect.x, 0)

    def test_negative_x_setter(self):
        """Attempts to set x to an int < 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10)
            rect.x = -2

    def test_string_x_setter(self):
        """Attempts to set x of type str"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.x = "2"

    def test_list_x_setter(self):
        """Attempts to set x of type list"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.x = [2]

    def test_tuple_x_setter(self):
        """Attempts to set x of type tuple"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.x = (12, )

    def test_set_x_setter(self):
        """Attempts to set x of type set"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.x = {12}

    def test_dictionary_x_setter(self):
        """Attempts to set x of type dict"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.x = {"x": 2}

    def test_zero_y_setter(self):
        """Attempts to set y to an int = 0"""
        rect = Rectangle(5, 10)
        rect.y = 0
        self.assertEqual(rect.y, 0)

    def test_negative_y_setter(self):
        """Attempts to set y to an int < 0"""
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10)
            rect.y = -2

    def test_string_y_setter(self):
        """Attempts to set y of type str"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.y = "2"

    def test_list_y_setter(self):
        """Attempts to set x of type list"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.y = [2]

    def test_tuple_y_setter(self):
        """Attempts to set y of type tuple"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.y = (12, )

    def test_set_y_setter(self):
        """Attempts to set x of type set"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.y = {12}

    def test_dictionary_y_setter(self):
        """Attempts to set x of type dict"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)
            rect.y = {"y": 2}


class TestRectangleArea(unittest.TestCase):
    """Tests the functionality of the Rectangle instance method area()"""

    def test_perfect_instance_area(self):
        """Tests a Rectangle instance area()"""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_unknown_object_area(self):
        """Tests the area() method on an undefined object"""
        with self.assertRaises(NameError):
            unknown_object.area()

    def test_instance_display(self):
        """Tests the display() method on a Rectangle instance"""
        rect = Rectangle(2, 2)
        self.assertEqual(rect.display(), None)


class TestRectangleStr(unittest.TestCase):
    """Tests the functionality of the __str__() method"""

    def test_all_args_str(self):
        """Tests the __str__() method on a Rectangle instance"""
        rect = Rectangle(4, 6, 2, 1, 12)
        strRet = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(rect.__str__(), strRet)

    def test_4_args_str(self):
        """Tests the __str__() method with 4 args"""
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(5, 10, 2, 2)
        strRet = "[Rectangle] (" + str((rect1.id + 1)) + ") 2/2 - 5/10"
        self.assertEqual(rect2.__str__(), strRet)

    def test_3_args_str(self):
        """Tests the __str__() method with 3 args"""
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(5, 10, 2)
        strRet = "[Rectangle] (" + str((rect1.id + 1)) + ") 2/0 - 5/10"
        self.assertEqual(rect2.__str__(), strRet)

    def test_2_args_str(self):
        """Tests the __str__() method with 2 args"""
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(5, 10)
        strRet = "[Rectangle] (" + str((rect1.id + 1)) + ") 0/0 - 5/10"
        self.assertEqual(rect2.__str__(), strRet)

    def test_set_all_args(self):
        """Tests the __str__() method after setting all the args"""
        rect = Rectangle(5, 10, 2, 2, 1)
        rect.width = 4
        rect.height = 6
        rect.x = 3
        rect.y = 1
        rect.id = 12
        self.assertEqual(rect.__str__(), "[Rectangle] (12) 3/1 - 4/6")


class TestRectangleUpdate(unittest.TestCase):
    """Tests the functionality of the update() method"""

    def test_1_arg_update(self):
        """Tests the update() method with one arg"""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual(str(rect), "[Rectangle] (89) 10/10 - 10/10")

    def test_2_args_update(self):
        """Tests the update() method with two args"""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2)
        self.assertEqual(str(rect), "[Rectangle] (89) 10/10 - 2/10")

    def test_3_args_update(self):
        """Tests the update() method with three args"""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3)
        self.assertEqual(str(rect), "[Rectangle] (89) 10/10 - 2/3")

    def test_4_args_update(self):
        """Tests the update() method with four args"""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/10 - 2/3")

    def test_5_args_update(self):
        """Tests the update() method with five args"""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")

    def test_1_kwargs_update(self):
        """Tests the update() method with one kwarg"""
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=1)
        self.assertEqual(str(rect), "[Rectangle] (10) 10/10 - 10/1")

    def test_2_kwargs_update(self):
        """Tests the update() method with two kwargs"""
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=1, x=2)
        self.assertEqual(str(rect), "[Rectangle] (10) 2/10 - 10/1")

    def test_3_kwargs_update(self):
        """Tests the update() method with three kwargs"""
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=1, x=2, width=3)
        self.assertEqual(str(rect), "[Rectangle] (10) 2/10 - 3/1")

    def test_4_kwargs_update(self):
        """Tests the update() method with four kwargs"""
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=1, x=2, width=3, y=2)
        self.assertEqual(str(rect), "[Rectangle] (10) 2/2 - 3/1")

    def test_5_kwargs_update(self):
        """Tests the update() method with five kwargs"""
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=1, x=2, width=3, y=2, id=89)
        self.assertEqual(str(rect), "[Rectangle] (89) 2/2 - 3/1")


class TestRectangleToDictionary(unittest.TestCase):
    """Tests the functionality of the Rectangle instance
    
    method to_dictionary()
    """

    def test_perfect_to_dictionary(self):
        """Tests the to_dictionary() method on a Rectangle instance"""
        rect1 = Rectangle(5, 10, 2, 2, 12)
        rect_dict = rect1.to_dictionary()
        rect2 = Rectangle(6, 12)
        rect2.update(**rect_dict)
        self.assertEqual(str(rect2), "[Rectangle] (12) 2/2 - 5/10")

    def test_unknown_object(self):
        "Test the to_dictionary() method on an undefined object"""
        with self.assertRaises(NameError):
            unknown_obj.to_dictionary()
