#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test with an unsorted list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_duplicate_max(self):
        """Test with duplicate max values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 5, -3, 8]), 8)

    def test_float_numbers(self):
        """Test with a list containing float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 0.8, 2.5]), 2.7)


if __name__ == '__main__':
    unittest.main()
