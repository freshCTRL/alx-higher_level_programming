#!/usr/bin/python3
"""
    THis module contain possible test cases for the
    class Base, Square, and Rectangle
"""
import unittest
from unittest import mock
from unittest.mock import patch
import io
import os
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
        sample1 = Square(1)
        self.assertEqual(sample1.size, 1)
        sample1 = Square(1, 2)
        self.assertEqual(sample1.to_dictionary(),
                         {'id': 27, 'size': 1, 'x': 2, 'y': 0})
        sample1 = Square(1, 2, 3)
        self.assertEqual(sample1.to_dictionary(),
                         {'id': 28, 'size': 1, 'x': 2, 'y': 3})
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -3)
        self.assertRaises(ValueError, Square, 0)
        self.assertEqual(str(sample1), '[Square] (28) 2/3 - 1')
        sample1.update()
        self.assertEqual(str(sample1), '[Square] (28) 2/3 - 1')
        sample1.update(99)
        self.assertEqual(str(sample1), '[Square] (99) 2/3 - 1')
        sample1.update(89, 1, 2, 3)
        self.assertEqual(str(sample1), '[Square] (89) 2/3 - 1')
        sample1.update(**{"id": 88, "size": 7})
        self.assertEqual(str(sample1), '[Square] (88) 2/3 - 7')
        val = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        sample1.update(**val)
        self.assertEqual(str(sample1), '[Square] (89) 2/3 - 1')
        sample2 = Square.create(**{'id': 89})
        self.assertEqual(str(sample2), '[Square] (89) 0/0 - 1')
        sample2 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(sample2), '[Square] (89) 2/0 - 1')
        sample2 = Square(1, 2, 3, 4)
        self.assertEqual(sample2.to_dictionary(),
                         {'id': 4, 'size': 1, 'x': 2, 'y': 3})
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])
        os.remove("Square.json")
        val = Square(1)
        Square.save_to_file([val])
        self.assertEqual(Square.load_from_file()[0].size, 1)
        os.remove("Square.json")
        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])
        os.remove("Square.json")

    def test_square_display(self):
        """
            tests display method
        """
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            sample4 = Square(1)
            sample4.display()
        assert fake_stdout.getvalue() == "#\n"
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            sample4 = Square(1, 2)
            sample4.display()
        assert fake_stdout.getvalue() == "  #\n"
