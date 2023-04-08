#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_e(self):
        # test for various conditions of argument passed
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([2, 2, 2]), 2)
        self.assertEqual(max_integer((2, 2, 2)), 2)
        self.assertEqual(max_integer("house"), "u")
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer([8,3,1]), 8)
        self.assertEqual(max_integer([3]), 3)
        self.assertRaises(TypeError, max_integer(), {1, 2, 3})
