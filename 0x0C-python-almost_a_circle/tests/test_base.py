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

if __name__ == '__main__':
    unittest.main()

