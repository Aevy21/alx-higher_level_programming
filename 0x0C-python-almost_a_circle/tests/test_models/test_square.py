""" Unit test for class Square """

import unittest
from models.square import Square


class TestSquareClassInstantiation(unittest.TestCase):
    """Tests variations of class Square instantiation"""

    def test_normal_Square(self):
        """Proper object instantiation with integer size > 0"""
        sq1 = Square(5)
        sq2 = Square(6)

        self.assertEqual(sq2.id, sq1.id + 1)
        self.assertEqual(sq1.width, 5)
        self.assertEqual(sq1.height, 5)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.y, 0)

    def test_unique_id(self):
        """Proper object instantiation with integer size > 0,

        and unique id
        """
        sq1 = Square(4)
        sq2 = Square(5, id=12)
        sq3 = Square(6)

        self.assertEqual(sq2.id, 12)
        self.assertEqual(sq3.id, sq1.id + 1)

    def test_unique_x(self):
        """Object instantiation with int x value >= 0"""
        sq1 = Square(5, x=1)
        sq2 = Square(6, x=15)

        self.assertEqual(sq1.x, 1)
        self.assertEqual(sq2.x, 15)

    def test_negative_x(self):
        """Object instantiation with int x value < 0"""
        with self.assertRaises(ValueError):
            Square(5, x=-5)

    def test_string_x(self):
        """Object instantiation with x of type str"""
        with self.assertRaises(TypeError):
            Square(5, "5")

    def test_list_x(self):
        """Object instantiation with x of type list"""
        with self.assertRaises(TypeError):
            Square(5, [5])

    def test_tuple_x(self):
        """Object instantiation with x of type tuple"""
        with self.assertRaises(TypeError):
            Square(5, (5, ))

    def test_set_x(self):
        """Object instantiation with x of type set"""
        with self.assertRaises(TypeError):
            Square(5, {3, 4})

    def test_dictionary_x(self):
        """Object instantiation with x of type dict"""
        with self.assertRaises(TypeError):
            Square(5, {"x": 5})

    def test_unique_y(self):
        """Object instantiation with int y value >= 0"""
        sq1 = Square(5, y=1)
        sq2 = Square(6, y=15)

        self.assertEqual(sq1.y, 1)
        self.assertEqual(sq2.y, 15)

    def test_negative_y(self):
        """Object instantiation with int y value < 0"""
        with self.assertRaises(ValueError):
            Square(5, y=-5)

    def test_string_y(self):
        """Object instantiation with y of type str"""
        with self.assertRaises(TypeError):
            Square(5, 2, "5")

    def test_list_y(self):
        """Object instantiation with y of type list"""
        with self.assertRaises(TypeError):
            Square(5, 2, [5])

    def test_tuple_y(self):
        """Object instantiation with y of type tuple"""
        with self.assertRaises(TypeError):
            Square(5, 2, (5, ))

    def test_set_y(self):
        """Object instantiation with y of type set"""
        with self.assertRaises(TypeError):
            Square(5, 2, {3, 4})

    def test_dictionary_y(self):
        """Object instantiation with y of type dict"""
        with self.assertRaises(TypeError):
            Square(5, 2, {"y": 5})

    def test_zero_size(self):
        """Instantiating Square class with size = 0"""
        with self.assertRaises(ValueError):
            sq = Square(0)

    def test_negative_size(self):
        """Instantiating Square class with size < 0"""
        with self.assertRaises(ValueError):
            sq = Square(-5)

    def test_string_size(self):
        """Object instantiation with size of type str"""
        with self.assertRaises(TypeError):
            Square("5")

    def test_list_size(self):
        """Object instantiation with size of type list"""
        with self.assertRaises(TypeError):
            Square([5])

    def test_tuple_size(self):
        """Object instantiation with size of type tuple"""
        with self.assertRaises(TypeError):
            Square((5, ))

    def test_set_size(self):
        """Object instantiation with size of type set"""
        with self.assertRaises(TypeError):
            Square({5})

    def test_dictionary_size(self):
        """Object instantiation with size of type dict"""
        with self.assertRaises(TypeError):
            Square({"size": 5})


class TestRectangleSetters(unittest.TestCase):
    """Tests the functionality of Square attribute setters"""

    def test_size_setter(self):
        """Sets size of a Square instance to an int > 0"""
        sq = Square(5)
        sq.size = 10
        self.assertEqual(sq.size, 10)

    def test_zero_size_setter(self):
        """Attempts to set size to an int = 0"""
        with self.assertRaises(ValueError):
            sq = Square(5)
            sq.size = 0

    def test_negative_size_setter(self):
        """Attempts to set size to an int < 0"""
        with self.assertRaises(ValueError):
            sq = Square(5)
            sq.size = -5

    def test_string_size_setter(self):
        """Attempts to set size of type str"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.size = "6"

    def test_list_size_setter(self):
        """Attempts to set size of type list"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.size = [6]

    def test_tuple_size_setter(self):
        """Attempts to set size of type tuple"""
        with self.assertRaises(TypeError): 
            sq = Square(5)
            sq.size = (6, )

    def test_set_size_setter(self):
        """Attempts to set size of type set"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.size = {6}

    def test_dictionary_size_setter(self):
        """Attempts to size of type dict"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.size = {"width": 6}

    def test_zero_x_setter(self):
        """Attempts to set x to an int = 0"""
        sq = Square(5)
        sq.x = 0
        self.assertEqual(sq.x, 0)

    def test_negative_x_setter(self):
        """Attempts to set x to an int < 0"""
        with self.assertRaises(ValueError):
            sq = Square(5)
            sq.x = -2

    def test_string_x_setter(self):
        """Attempts to set x of type str"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.x = "2"

    def test_list_x_setter(self):
        """Attempts to set x of type list"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.x = [2]

    def test_tuple_x_setter(self):
        """Attempts to set x of type tuple"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.x = (2, )

    def test_set_x_setter(self):
        """Attempts to set x of type set"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.x = {2}

    def test_dictionary_x_setter(self):
        """Attempts to set x of type dict"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.x = {"x": 2}

    def test_zero_y_setter(self):
        """Attempts to set y to an int = 0"""
        sq = Square(5)
        sq.y = 0
        self.assertEqual(sq.y, 0)

    def test_negative_y_setter(self):
        """Attempts to set y to an int < 0"""
        with self.assertRaises(ValueError):
            sq = Square(5)
            sq.y = -2

    def test_string_y_setter(self):
        """Attempts to set y of type str"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.y = "2"

    def test_list_y_setter(self):
        """Attempts to set x of type list"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.y = [2]

    def test_tuple_y_setter(self):
        """Attempts to set y of type tuple"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.y = (2, )

    def test_set_y_setter(self):
        """Attempts to set x of type set"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.y = {2}

    def test_dictionary_y_setter(self):
        """Attempts to set x of type dict"""
        with self.assertRaises(TypeError):
            sq = Square(5)
            sq.y = {"y": 2}


class TestSquareArea(unittest.TestCase):
    """Tests the functionality of the inherited Square instance method @area"""

    def test_perfect_instance_area(self):
        """Tests a Square instance area"""
        sq = Square(5)
        self.assertEqual(sq.area(), 25)

    def test_unknown_object_area(self):
        """Tests the @area method on an undefined object"""
        with self.assertRaises(NameError):
            unknown_object.area()

    def test_instance_display(self):
        """Tests the @display method on a Square instance"""
        sq = Square(2)
        self.assertEqual(sq.display(), None)


class TestSquareStr(unittest.TestCase):
    """Tests the functionality of the __str__ method"""

    def test_all_args_str(self):
        """Tests the __str__ method on a Rectangle instance"""
        sq = Square(4, 2, 1, 12)
        strRet = "[Square] (12) 2/1 - 4"
        self.assertEqual(sq.__str__(), strRet)

    def test_3_args_str(self):
        """Tests the __str__ method with 4 args"""
        sq1 = Square(2)
        sq2 = Square(5, 2, 2)
        strRet = "[Square] (" + str((sq1.id + 1)) + ") 2/2 - 5"
        self.assertEqual(sq2.__str__(), strRet)

    def test_2_args_str(self):
        """Tests the __str__ method with 3 args"""
        sq1 = Square(2)
        sq2 = Square(5, 2)
        strRet = "[Square] (" + str((sq1.id + 1)) + ") 2/0 - 5"
        self.assertEqual(sq2.__str__(), strRet)

    def test_1_args_str(self):
        """Tests the __str__ method with 2 args"""
        sq1 = Square(2)
        sq2 = Square(5)
        strRet = "[Square] (" + str((sq1.id + 1)) + ") 0/0 - 5"
        self.assertEqual(sq2.__str__(), strRet)

    def test_set_all_args(self):
        """Tests the __str__ method after setting all the args"""
        sq = Square(5, 2, 2, 1)
        sq.size = 4
        sq.x = 3
        sq.y = 1
        sq.id = 12
        self.assertEqual(sq.__str__(), "[Square] (12) 3/1 - 4")


class TestSquareUpdate(unittest.TestCase):
    """Tests the functionality of the @update method"""

    def test_1_arg_update(self):
        """Tests the update method with one arg"""
        sq = Square(5, id=10)
        sq.update(1)
        self.assertEqual(sq.__str__(), "[Square] (1) 0/0 - 5")

    def test_2_args_update(self):
        """Tests the update method with two args"""
        sq = Square(5, id=10)
        sq.update(1, 2)
        self.assertEqual(sq.__str__(), "[Square] (1) 0/0 - 2")

    def test_3_args_update(self):
        """Tests the update method with three args"""
        sq = Square(5, id=10)
        sq.update(1, 2, 3)
        self.assertEqual(sq.__str__(), "[Square] (1) 3/0 - 2")

    def test_4_args_update(self):
        """Tests the update method with four args"""
        sq = Square(5, id=10)
        sq.update(1, 2, 3, 4)
        self.assertEqual(sq.__str__(), "[Square] (1) 3/4 - 2")

    def test_1_kwargs_update(self):
        """Tests the update method with one kwarg"""
        sq = Square(5, 2, 2, 1)
        sq.update(x=12)
        self.assertEqual(sq.__str__(), "[Square] (1) 12/2 - 5")

    def test_2_kwargs_update(self):
        """Tests the update method with two kwargs"""
        sq = Square(5, 2, 2, 1)
        sq.update(x=12, size=10)
        self.assertEqual(sq.__str__(), "[Square] (1) 12/2 - 10")

    def test_3_kwargs_update(self):
        """Tests the update method with three kwargs"""
        sq = Square(5, 2, 2, 1)
        sq.update(x=12, size=10, id=2)
        self.assertEqual(sq.__str__(), "[Square] (2) 12/2 - 10")

    def test_4_kwargs_update(self):
        """Tests the update method with four kwargs"""
        sq = Square(5, 2, 2, 1)
        sq.update(x=12, size=10, id=2, y=3)
        self.assertEqual(sq.__str__(), "[Square] (2) 12/3 - 10")


class TestSquareToDictionary(unittest.TestCase):
    """Tests the functionality of the Square instance

    method to_dictionary()
    """

    def test_perfect_to_dictionary(self):
        """Tests the to_dictionary() method on a Square instance"""
        sq1 = Square(5, 2, 2, 12)
        sq_dict = sq1.to_dictionary()
        sq2 = Square(6)
        sq2.update(**sq_dict)
        self.assertEqual(str(sq2), "[Square] (12) 2/2 - 5")

    def test_unknown_object(self):
        "Test the to_dictionary() method on an undefined object"""
        with self.assertRaises(NameError):
            unknown_obj.to_dictionary()
