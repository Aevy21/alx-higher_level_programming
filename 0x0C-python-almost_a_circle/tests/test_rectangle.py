import unittest
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):

    def test_default_attributes(self):
        # Test default attributes and inheritance from Base
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNotNone(rect.id)

    def test_explicit_attributes(self):
        # Test explicit attributes and inheritance from Base
        rect = Rectangle(5, 10, 2, 3, id=15)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 15)

    def test_set_attributes(self):
        # Test setting attributes
        rect = Rectangle(5, 10)
        rect.width = 15
        rect.height = 20
        rect.x = 3
        rect.y = 5
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 5)

    def test_invalid_width(self):
        # Test invalid width
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_invalid_height(self):
        # Test invalid height
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

    def test_invalid_x(self):
        # Test invalid x
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, x=-2)

    def test_invalid_y(self):
        # Test invalid y
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, y=-3)

    def test_invalid_type(self):
        # Test invalid type for width
        with self.assertRaises(TypeError):
            rect = Rectangle("5", 10)

    def test_set_invalid_width(self):
        # Test setting invalid width
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rect.width = -15

    def test_set_invalid_x(self):
        # Test setting invalid x
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rect.x = -3

if __name__ == '__main__':
    unittest.main()

