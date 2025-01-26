#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    # Test avec des entiers
    def test_max_integer_with_integers(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    
    # Test avec des flottants
    def test_max_integer_with_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
if __name__ == '__main__':
    unittest.main()