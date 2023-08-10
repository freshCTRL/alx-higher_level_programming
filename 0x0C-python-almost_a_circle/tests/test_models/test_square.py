#!/usr/bin/python3
"""
    THis module contain possible test cases for the
    class Base, Square, and Rectangle
"""
import unittest
from models.square import Square


class Test_3(unittest.TestCase):

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

    def test_Square(self):
        """
            THis test definition tests all the possible test cases
            on class Square
        """
        self.assertIsNotNone(Square(1))
        self.assertIsNotNone(Square(1, 2))
        self.assertIsNotNone(Square(1, 2, 3))
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        self.assertRaises(ValueError, Square, 0)
        self.assertIsNotNone(str(Square))
        self.assertIsNotNone(Square(1, 2, 3).to_dictionary())
        self.assertIsNone(Square(1, 2, 3).update())
        self.assertIsNone(Square(1, 2, 3).update(99))
        self.assertIsNone(Square(1, 2, 3).update(89, 1))
        self.assertIsNone(Square(1, 2, 3).update(89, 1, 2, 3))
        self.assertIsNone(Square(1, 2, 3).update(**{"id": 89}))
        self.assertIsNone(Square(1, 2, 3).update(**{"id": 89, "size": 1}))
        value = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        self.assertIsNone(Square(1, 2, 3).update(**value))
        self.assertIsNotNone(Square.create(**{'id': 89}))
        self.assertIsNotNone(Square.create(**{'id': 89, 'size': 1}))
        self.assertIsNotNone(Square.create(**{'id': 89, 'size': 1, 'x': 2}))
        self.assertIsNotNone(Square.create(**value))
        self.assertEqual(Square.load_from_file(), [])
        self.assertIsNone(Square.save_to_file(None))
        self.assertIsNone(Square.save_to_file([]))
        self.assertIsNone(Square.save_to_file([Square(1)]))
        self.assertIsNotNone(Square.load_from_file())
