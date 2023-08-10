#!/usr/bin/python3
"""
THis module contain possible test cases for the
class Base, Square, and Rectangle
"""
import unittest
from models.rectangle import Rectangle


class Test_2(unittest.TestCase): 
    """
    this is a test class containing all
    possible test cases
    """
    def setUp(self):
        """
        initialises a test...
        """
        pass
    def test_Rectangle(self):
        """
        THis test definition tests all the possible test cases
        on class Rectangle
        """
        valu = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        ist_2r = Rectangle(1, 2)
        ist_1r = Rectangle(1, 2, 3)
        self.assertIsNotNone(Rectangle(1, 2))
        self.assertIsNotNone(Rectangle(1, 2, 3))
        self.assertIsNotNone(Rectangle(1, 2, 3, 4))
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        self.assertRaises(TypeError, Rectangle, 2, "1")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)
        self.assertIsNotNone(ist_2r.area())
        self.assertIsNotNone(str(ist_2r))
        self.assertIsNotNone(ist_1r.to_dictionary())
        self.assertIsNone(ist_1r.update())
        self.assertIsNone(ist_1r.update(78))
        self.assertIsNone(ist_1r.update(78, 1))
        self.assertIsNone(ist_1r.update(78, 1, 2))
        self.assertIsNone(ist_1r.update(78, 1, 2, 3))
        self.assertIsNone(ist_1r.update(78, 1, 2, 3, 4))
        self.assertIsNone(ist_1r.update(**{"id": 89}))
        self.assertIsNone(ist_1r.update(**{"id": 89, "width": 1}))
        self.assertIsNone(ist_1r.update(**{"id": 89, "width": 1, "height": 2}))
        self.assertIsNone(ist_1r.update(**valu))
        self.assertIsNotNone(Rectangle.create(**{"id": 89}))
        self.assertIsNotNone(Rectangle.create(**{"id": 89, "width": 1}))
        self.assertIsNotNone(Rectangle.create(**{"id": 89, "width": 1, "height": 2}))
        self.assertIsNotNone(Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3}))
        self.assertIsNotNone(Rectangle.create(**valu))
        self.assertIsNone(Rectangle.save_to_file(None))
        self.assertIsNone(Rectangle.save_to_file([]))
        self.assertIsNone(Rectangle.save_to_file([Rectangle(1, 2)]))
        self.assertIsNone(Rectangle.save_to_file([Rectangle(1, 2)]))
        self.assertIsNotNone(Rectangle.load_from_file())
    def tearDown(self):
        """
        closing a test...
        """
        pass
