#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_basic_usage(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5, "Should return the maximum integer in the list")

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, "Should return None for an empty list")

    def test_negative_numbers(self):
        result = max_integer([-5, -3, -8, -1])
        self.assertEqual(result, -1, "Should correctly handle negative numbers")

    def test_mixed_numbers(self):
        result = max_integer([10, -2, 8, 0])
        self.assertEqual(result, 10, "Should handle a mix of positive and negative numbers")

if __name__ == '__main__':
    unittest.main()

