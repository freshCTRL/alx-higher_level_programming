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

    def tearDown(self):
        """
        closing a test...
        """
        pass

    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(id=None)
        b4 = Base(id=99)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 99)
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')
        self.assertIsInstance(Base.to_json_string([{"id": 12}]), str)

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{"id": 12}])
        self.assertIsInstance(Base.from_json_string('[{"id": 12}]'), list)
