import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def setUp(self):
        # Reset the __nb_objects counter before each test
        Base._Base__nb_objects = 0

    def test_auto_incremented_id(self):
        obj1 = Base()
        obj2 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_explicit_id(self):
        obj1 = Base(id=10)
        obj2 = Base(id=20)

        self.assertEqual(obj1.id, 10)
        self.assertEqual(obj2.id, 20)

    def test_mixed_ids(self):
        obj1 = Base()
        obj2 = Base(id=100)
        obj3 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 100)
        self.assertEqual(obj3.id, 2)

    def test_negative_id(self):
        obj = Base(id=-5)
        self.assertEqual(obj.id, -5)

    def test_zero_id(self):
        obj = Base(id=0)
        self.assertEqual(obj.id, 0)

    def test_set_custom_id(self):
        obj = Base()
        obj.id = 12
        self.assertEqual(obj.id, 12)

    def test_unique_ids(self):
        objects = [Base() for _ in range(1000)]
        unique_ids = set(obj.id for obj in objects)

        self.assertEqual(len(objects), len(unique_ids))
    
class TestBaseClassExtended(unittest.TestCase):

    def test_auto_incremented_id_after_reset(self):
        obj1 = Base()
        obj2 = Base()

        # Reset the __nb_objects counter
        Base._Base__nb_objects = 0

        obj3 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 1)  # Auto-increment should start from 1 after reset

    def test_save_to_file_empty_list(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter
        objects = []

        # Save an empty list to a file
        Base.save_to_file(objects)

        with open("Base.json", 'r') as file:
            content = file.read()

        self.assertEqual(content, "[]")

    def test_load_from_file_nonexistent_file(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Try loading from a nonexistent file
        loaded_objects = Base.load_from_file()

        self.assertEqual(loaded_objects, [])

    def test_load_from_file_invalid_json(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Create an invalid JSON file
        with open("Base.json", 'w') as file:
            file.write("Invalid JSON")

        # Try loading from the invalid JSON file
        loaded_objects = Base.load_from_file()

        self.assertEqual(loaded_objects, [])

    def test_create_with_invalid_class(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Try creating an instance with an unsupported class
        with self.assertRaises(ValueError):
            invalid_instance = Base.create(width=5, height=10)

    def test_create_with_dictionary(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Create an instance using the create method with a dictionary
        instance_dict = {'id': 1, 'size': 5}
        created_instance = Base.create(**instance_dict)

        self.assertEqual(created_instance.id, 1)
        self.assertEqual(created_instance.size, 5)  # Assuming there is a 'size' attribute in the class
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Try creating an instance using the create method with a dictionary missing 'id'
        instance_dict = {'size': 5}
        created_instance = Base.create(**instance_dict)

        self.assertEqual(created_instance.id, 1)  # Default auto-incremented value should be used
        self.assertEqual(created_instance.size, 5)  # Assuming there is a 'size' attribute in the class

    def test_from_json_string_empty_string(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Try loading from an empty JSON string
        loaded_objects = Base.from_json_string("")

        self.assertEqual(loaded_objects, [])

    def test_set_custom_id_negative_value(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Try setting a custom ID with a negative value
        obj = Base()
        obj.id = -5

        self.assertEqual(obj.id, -5)

    def test_set_custom_id_zero_value(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Try setting a custom ID with a zero value
        obj = Base()
        obj.id = 0

        self.assertEqual(obj.id, 0)

    def test_to_json_string_invalid_input(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Try converting an invalid input to a JSON string
        invalid_input = None
        json_string = Base.to_json_string(invalid_input)

        self.assertEqual(json_string, "[]")

    def test_load_from_file_multiple_instances(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Create and save multiple instances to a file
        obj1 = Base()
        obj2 = Base()
        Base.save_to_file([obj1, obj2])

        # Load instances from the file
        loaded_objects = Base.load_from_file()

        self.assertEqual(len(loaded_objects), 2)
        self.assertEqual(loaded_objects[0].id, 1)
        self.assertEqual(loaded_objects[1].id, 2) 
    
    def test_create_with_dictionary_unsupported_class(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Try creating an instance using the create method with an unsupported class
        instance_dict = {'width': 5, 'height': 10}  # Assuming Rectangle attributes
        with self.assertRaises(ValueError) as context:
            created_instance = Base.create(**instance_dict)

        # Assert that the expected exception is raised
        self.assertEqual(
            str(context.exception), "Unsupported class for create method"
        )

    def test_create_with_unsupported_class(self):
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter

        # Try creating an instance using the create method with an unsupported class
        instance_dict = {'width': 5, 'height': 10}  # Assuming Rectangle attributes
        with self.assertRaises(ValueError) as context:
            created_instance = Base.create(**instance_dict)

        # Assert that the expected exception is raised with the correct message
        expected_error_message = "Unsupported class for create method"
        self.assertEqual(str(context.exception), expected_error_message)

if __name__ == '__main__':
    unittest.main()

