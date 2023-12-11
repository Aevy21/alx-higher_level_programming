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

    def test_area_calculation(self):
         # Test area calculation with additional cases
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


    def test_display_method(self):
        # Test display method
        r1 = Rectangle(4, 6)
        expected_output_r1 = ''.join(['#' * r1.width + '\n' for _ in range(r1.height)])
        with self.assertLogs() as cm:
            r1.display()
            self.assertEqual(cm.output, [expected_output_r1])

        r2 = Rectangle(2, 2)
        expected_output_r2 = "##\n##\n"
        with self.assertLogs() as cm:
            r2.display()
            self.assertEqual(cm.output, [expected_output_r2])
        
        # Test with width and height set to zero
        r3 = Rectangle(0, 0, 3, 4)
        expected_output_r3 = ""
        with self.assertLogs() as cm:
            r3.display()
            self.assertEqual(cm.output, [expected_output_r3])

        # Test with negative x and y values
        r4 = Rectangle(3, 2, -1, -2)
        expected_output_r4 = "\n\n ###\n ###\n"
        with self.assertLogs() as cm:
            r4.display()
            self.assertEqual(cm.output, [expected_output_r4])
    
    def test_set_width_to_zero(self):
        # Test setting width to 0
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_set_height_to_zero(self):
        # Test setting height to 0
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rect.height = 0
    
    def test_set_width_to_zero(self):
        # Test setting width to 0
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10)

    def test_set_height_to_zero(self):
        # Test setting height to 0
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 0)



    def test_str_method(self):
        # Test __str__ method with additional cases
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_str_r1 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected_str_r1)

        r2 = Rectangle(5, 5, 1)
        expected_str_r2 = "[Rectangle] ({}) 1/0 - 5/5".format(r2.id)
        self.assertEqual(str(r2), expected_str_r2)

        # Test with width and height set to zero
        r3 = Rectangle(1, 1, 3, 4, 15)
        expected_str_r3 = "[Rectangle] (15) 3/4 - 1/1"
        self.assertEqual(str(r3), expected_str_r3)

        # Test with negative x and y values
        with self.assertRaises(ValueError):
            r4 = Rectangle(3, 2, -1, -2, 20)

        # Test with maximum integer values
        r5 = Rectangle(2147483647, 2147483647, 0, 0, 999)
        expected_str_r5 = "[Rectangle] (999) 0/0 - 2147483647/2147483647"
        self.assertEqual(str(r5), expected_str_r5)


    def test_update_method(self):
        # Test update method with additional cases
        r1 = Rectangle(10, 10, 10, 10)
        expected_str_r1 = "[Rectangle] (10) 10/10 - 10/10"

        r1.update(89)
        expected_str_r1_updated_1 = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(str(r1), expected_str_r1_updated_1)

        r1.update(89, 2)
        expected_str_r1_updated_2 = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(str(r1), expected_str_r1_updated_2)

        r1.update(89, 2, 3)
        expected_str_r1_updated_3 = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(str(r1), expected_str_r1_updated_3)

        r1.update(89, 2, 3, 4)
        expected_str_r1_updated_4 = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(str(r1), expected_str_r1_updated_4)
        
        r1.update(89, 2, 3, 4, 5)
        expected_str_r1_updated_5 = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str(r1), expected_str_r1_updated_5)

        # Test update method with invalid values
        with self.assertRaises(ValueError):
            r1.update(89, -2, 3, 4, 5)

        with self.assertRaises(ValueError):
            r1.update(89, 2, 3, -4, 5)

        # Test update method with invalid type
        with self.assertRaises(TypeError):
            r1.update(89, "2", 3, 4, 5)

        with self.assertRaises(TypeError):
            r1.update(89, 2, "3", 4, 5)
    
        r1.update(width=1, x=2)
        expected_str_r1_updated_2 = "[Rectangle] (10) 2/10 - 1/1"
        self.assertEqual(str(r1), expected_str_r1_updated_2)

        r1.update(y=1, width=2, x=3, id=89)
        expected_str_r1_updated_3 = "[Rectangle] (89) 3/1 - 2/1"
        self.assertEqual(str(r1), expected_str_r1_updated_3)

        r1.update(x=1, height=2, y=3, width=4)
        expected_str_r1_updated_4 = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(str(r1), expected_str_r1_updated_4)

        # Test update method with invalid values
        with self.assertRaises(ValueError):
            r1.update(width=-2, x=3)

        with self.assertRaises(ValueError):
            r1.update(y=1, width=2, x=-3)

        # Test update method with invalid type
        with self.assertRaises(TypeError):
            r1.update(width="2", x=3)

        with self.assertRaises(TypeError):
            r1.update(y=1, width=2, x="3")
    
if __name__ == '__main__':
    unittest.main()


