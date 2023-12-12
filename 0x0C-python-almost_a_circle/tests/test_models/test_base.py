import unittest
import json
from your_module import Base, Rectangle


class TestBaseClass(unittest.TestCase):

    def setUp(self):
        # This method is called before each test method
        Base._Base__nb_objects = 0  # Reset the private class attribute before each test

    def test_object_creation(self):
        # Test basic object creation and ID assignment
        obj1 = Base()
        self.assertEqual(obj1.id, 1)  # Assuming the first object should have ID 1

        obj2 = Base()
        self.assertEqual(obj2.id, 2)  # Assuming the second object should have ID 2

    def test_custom_starting_id(self):
        # Test if the class allows specifying a custom starting ID
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
    def test_zero_starting_id(self):
        # Test if the class handles a starting ID of zero gracefully
        b1 = Base(0)
        self.assertEqual(b1.id, 1)  # ID should default to 1 if starting from zero

    def test_non_integer_id(self):
        # Test if the class handles a non-integer ID gracefully
        with self.assertRaises(TypeError):
            Base("string_id")  # Should raise a TypeError for a non-integer ID


    def test_private_class_attribute(self):
        # Test that the private class attribute __nb_objects is not accessible directly
        self.assertNotIn('__nb_objects', dir(Base))

    def test_custom_starting_id(self):
        # Test if the class allows specifying a custom starting ID
        obj_with_custom_id = Base(100)
        self.assertEqual(obj_with_custom_id.id, 100)

    def test_negative_starting_id(self):
        # Test if the class handles a negative starting ID gracefully
        obj_with_negative_id = Base(-5)
        self.assertEqual(obj_with_negative_id.id, 1)  # ID should default to 1 if negative

    def test_invalid_starting_id_type(self):
        # Test if the class handles an invalid starting ID type gracefully
        with self.assertRaises(TypeError):
            Base("invalid")  # Should raise a TypeError for an invalid starting ID

    def test_auto_increment_id(self):
        # Test if the class auto-increments the ID when id is not provided
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)


    #test cases for the static method to_json_string
    def test_to_json_string_empty_list(self):
        # Test if the method returns "[]" for an empty list
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none_list(self):
        # Test if the method returns "[]" for None
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]") 

    def test_to_json_string_non_empty_list(self):
        # Test if the method correctly converts a non-empty list of dictionaries to JSON string
        input_list = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        expected_result = json.dumps(input_list)
        result = Base.to_json_string(input_list)
        self.assertEqual(result, expected_result)

    def test_to_json_string_rectangle_instance(self):
        # Test if the method correctly converts a Rectangle instance to JSON string
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

    self.assertTrue(isinstance(json_dictionary, str))
        self.assertEqual(type(dictionary), dict)

#Test cases for the save_to_file method
     def tearDown(self):
        # This method is called after each test method
        # Clean up any created files
        file_name = "{}.json".format(Base.__name__)
        if os.path.exists(file_name):
            os.remove(file_name)
        

    def test_save_to_file_empty_list(self):
        # Test if the method creates an empty file for an empty list
        Base.save_to_file([])
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_none_list(self):
        # Test if the method creates an empty file for None
        Base.save_to_file(None)
        self.assertTrue(os.path.exists("Base.json"))
        with open("Base.json", 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")

    
    def test_save_to_file_non_empty_list(self):
        # Test if the method correctly writes a non-empty list to a file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 4, 1, 2)
        Base.save_to_file([r1, r2])

        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r') as file:
            content = file.read()
            # Ensure the content is a JSON representation of the list of dictionaries
            self.assertIn('{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}', content)
            self.assertIn('{"id": 2, "width": 5, "height": 4, "x": 1, "y": 2}', content)

      def test_save_to_file_invalid_list_element(self):
        # Test if the method handles an invalid list element gracefully
        with self.assertRaises(AttributeError):
            Base.save_to_file([42])  # Raises AttributeError because 42 has no to_dictionary method

    def test_save_to_file_invalid_list_type(self):
        # Test if the method handles an invalid list type gracefully
        with self.assertRaises(TypeError):
            Base.save_to_file("not_a_list")  # Raises TypeError because input is not a list

    def test_save_to_file_instance_with_to_json_string(self):
        # Test if the method correctly writes an instance with to_json_string method to a file
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        # Ensure the file is created and contains the expected JSON content
        Base.save_to_file([r1])

        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r') as file:
            content = file.read()
            self.assertEqual(content, json_dictionary)

#Tests case for from_json_string
    def test_from_json_string_empty_string(self):
        # Test if the method returns an empty list for an empty string
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_none_string(self):
        # Test if the method returns an empty list for None
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_valid_json_string(self):
        # Test if the method correctly converts a valid JSON string to a list
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        expected_result = json.loads(json_string)
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)

    def test_from_json_string_invalid_json_string(self):
        # Test if the method handles an invalid JSON string gracefully
        with self.assertRaises(json.JSONDecodeError):
            Base.from_json_string("invalid_json")  # Raises JSONDecodeError for an invalid JSON string

    def test_from_json_string_rectangle_instance(self):
        # Test if the method correctly converts a JSON string to a list containing Rectangle instances
        list_input = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertEqual(type(list_output), list)
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in list_output))

#Test case for create class method

    def test_create_rectangle_instance(self):
        # Test if the create method correctly creates a Rectangle instance
        rect_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        rect_instance = Rectangle.create(**rect_dict)

        # Add assertions based on your expectations
        self.assertIsInstance(rect_instance, Rectangle)
        self.assertEqual(rect_instance.to_dictionary(), rect_dict)

    def test_create_square_instance(self):
        # Test if the create method correctly creates a Square instance
        square_dict = {'id': 2, 'size': 7, 'x': 1, 'y': 4}
        square_instance = Square.create(**square_dict)
        
        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.to_dictionary(), square_dict)
    
    def test_create_invalid_class(self):
        # Test if the create method raises a ValueError for an unsupported class
        with self.assertRaises(ValueError):
            Base.create(id=1, name="Alice")  # Raises ValueError for an unsupported class

    def test_create_instance_from_to_dictionary(self):
        # Test if the create method correctly creates an instance from its to_dictionary representation
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsInstance(r2, Rectangle)
        self.assertNotEqual(r1, r2)  # Ensure r1 and r2 are not the same instance
        self.assertEqual(r1, r2)  # Ensure r1 and r2 are equivalent in terms of attributes

#test case for load_from_file class method


def test_load_from_file_empty_file(self):
        # Test if the method returns an empty list for an empty file
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_non_empty_file(self):
        # Test if the method correctly loads instances from a non-empty file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 4, 1, 2)
        Rectangle.save_to_file([r1, r2])

        result = Rectangle.load_from_file()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Rectangle)
        self.assertIsInstance(result[1], Rectangle)
        self.assertEqual(result[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(result[1].to_dictionary(), r2.to_dictionary())

    def test_load_from_nonexistent_file(self):
        # Test if the method returns an empty list for a nonexistent file
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])


    def tearDown(self):
        # This method is called after each test method
        # Clean up any created files
        file_name_rect = "{}.json".format(Rectangle.__name__)
        if os.path.exists(file_name_rect):
            os.remove(file_name_rect)

        file_name_square = "{}.json".format(Square.__name__)
        if os.path.exists(file_name_square):
            os.remove(file_name_square)

    def test_save_and_load_rectangles(self):
        # Test if saving and loading rectangles works as expected
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        # Add assertions based on your expectations
        self.assertIsInstance(list_rectangles_output, list)
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)
        self.assertEqual(list_rectangles_output[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(list_rectangles_output[1].to_dictionary(), r2.to_dictionary())

     def test_save_and_load_squares(self):
        # Test if saving and loading squares works as expected
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        # Add assertions based on your expectations
        self.assertIsInstance(list_squares_output, list)
        self.assertEqual(len(list_squares_output), 2)
        self.assertIsInstance(list_squares_output[0], Square)
        self.assertIsInstance(list_squares_output[1], Square)
        self.assertEqual(list_squares_output[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(list_squares_output[1].to_dictionary(), s2.to_dictionary())


if __name__ == '__main__':
    unittest.main()

