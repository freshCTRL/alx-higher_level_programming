#!/usr/bin/python3
"""
    THis module contain possible test cases for the
    class Base, Square, and Rectangle
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    this is a test class containing all
    possible test cases
    """

    def setUp(self):
        """
        initialising a test...
        """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """
        closing a test...
        """
        Base._Base__nb_objects = 0

    def test_instantiation_with_no_arg(self):
        b1 = Base()

        self.assertEqual(b1.id, 1)

    def test_instantiation_with_none_value(self):
        b2 = Base(None)

        self.assertEqual(b2.id, 1)

    def test_instantiation_with_arg(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_instantiation_set_value_based_on_previous_value(self):
        b4 = Base()
        b5 = Base()

        self.assertEqual(b5.id, b4.id + 1)

    def test_to_json_string(self):
        """
        tests to_json_string method
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')
        self.assertIsInstance(Base.to_json_string([{"id": 12}]), str)

    def test_from_json_string(self):
        """
        tests from_json_string method
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{"id": 12}])
        self.assertIsInstance(Base.from_json_string('[{"id": 12}]'), list)


if __name__ == "main":
    unittest.main()
