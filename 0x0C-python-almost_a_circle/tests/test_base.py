#!/usr/bin/python3
"""
THis module contain possible test cases for the
class Base, Square, and Rectangle
"""
import unittest
from models.base import Base


class Test_1(unittest.TestCase):
    """
    this is a test class containing all
    possible test cases
    """
    def setUp(self):
        """
        initialising a test...
        """
        pass
    def test_Base(self):
        """
        THis test definition tests all the possible test cases
        on class Base
        """
        b1 = Base()
        b2 = Base()
        ist_3 = Base(99)
        self.assertTrue(b1.id == 1)
        self.assertTrue(b2.id == 2)
        self.assertEqual(ist_3.id, 99)
        self.assertIsNotNone(ist_3.to_json_string(None))
        self.assertIsNotNone(ist_3.to_json_string([]))
        self.assertIsNotNone(ist_3.to_json_string([{'id': 12}]))
        self.assertIsInstance(ist_3.to_json_string([{'id': 12}]), str)
        self.assertIsNotNone(ist_3.from_json_string(None))
        self.assertIsNotNone(ist_3.from_json_string("[]"))
        self.assertIsNotNone(ist_3.from_json_string('[{"id": 12}]'))
        self.assertIsInstance(ist_3.from_json_string('[{"id": 12}]'), list)
    def tearDown(self):
        """
        closing a test...
        """
        pass
