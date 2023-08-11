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

    def tearDown(self):
        """
            closing a test...
        """
        pass

    def test_Rectangle(self):
        """
            THis test definition tests all the possible test cases
            on class Rectangle
        """
        sample1 = Rectangle(1, 2)
        self.assertEqual(sample1.to_dictionary(),
                         {'id': 1, 'width': 1, 'height': 2, 'x': 0, 'y': 0})
        sample1 = Rectangle(1, 2, 3)
        self.assertEqual(sample1.to_dictionary(),
                         {'id': 2, 'width': 1, 'height': 2, 'x': 3, 'y': 0})
        sample1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(sample1.to_dictionary(),
                         {'id': 3, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        sample1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(sample1.to_dictionary(),
                         {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
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
        sample2 = Rectangle(1, 2)
        self.assertEqual(sample2.area(), 2)
        self.assertEqual(str(sample2), '[Rectangle] (1) 0/0 - 1/2')
        sample2 = Rectangle(1, 2, 3)
        self.assertEqual(sample2.to_dictionary(),
                         {'id': 2, 'width': 1, 'height': 2, 'x': 3, 'y': 0})
        sample2.update()
        self.assertEqual(str(sample2), '[Rectangle] (2) 3/0 - 1/2')
        sample2.update(78)
        self.assertEqual(str(sample2), '[Rectangle] (78) 3/0 - 1/2')
        sample2.update(78, 1)
        self.assertEqual(str(sample2), '[Rectangle] (2) 3/0 - 1/2')
        sample2.update(78, 1, 2)
        self.assertEqual(str(sample2), '[Rectangle] (78) 3/0 - 1/2')
        sample2.update(78, 1, 2, 3)
        self.assertEqual(str(sample2), '[Rectangle] (2) 3/0 - 1/2')
        sample2.update(78, 1, 2, 3, 4)
        self.assertEqual(str(sample2), '[Rectangle] (78) 3/0 - 1/2')
        sample2.update(**{"id": 89})
        self.assertEqual(str(sample2), '[Rectangle] (89) 3/0 - 1/2')
        sample2.update(**{"id": 89, "width": 1})
        self.assertEqual(str(sample2), '[Rectangle] (2) 3/0 - 1/2')
        sample2.update(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(str(sample2), '[Rectangle] (2) 3/0 - 1/2')
        val = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        sample2.update(**val)
        self.assertEqual(str(sample2), '[Rectangle] (89) 3/4 - 1/2')
        sample3 = Rectangle.create(**{"id": 89})
        self.assertEqual(str(sample3), '[Rectangle] (89) 0/0 - 1/1')
        sample3 = Rectangle.create(**{"id": 89, "width": 2})
        self.assertEqual(str(sample3), '[Rectangle] (89) 0/0 - 2/1')
        sample3 = Rectangle.create(**{"id": 89, "width": 2, "height": 2})
        self.assertEqual(str(sample3), '[Rectangle] (89) 0/0 - 2/2')
        val = {"id": 89, "width": 2, "height": 2, "x": 3, "y": 4}
        sample3 = Rectangle.create(**val)
        self.assertEqual(str(sample3), '[Rectangle] (89) 3/4 - 2/2')
        val = None
        sample3.save_to_file(val)
        self.assertTrue(sample3.load_from_file() == [])
        val = []
        sample3.save_to_file(val)
        self.assertTrue(sample3.load_from_file() == val)
        val = [Rectangle(1, 2)]
        sample3.save_to_file(val)
        self.assertIsInstance(sample3.load_from_file(), list)
        # self.assertIsNone(sample3.save_to_file())
